import json
import sys
from pathlib import Path

# Add parent directory to Python path
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils.proxy_tool import ProxyTool

import getpass
import os


def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


# Set google api key
_set_env("DASHSCOPE_API_KEY")
# Set tavily api key
_set_env("TAVILY_API_KEY")

# Set and enable proxy
# ProxyTool.set_proxy()
# ProxyTool.enable_proxy()

from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_community.llms import Tongyi
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver

# Custom state model
class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]

# Set up the Tongyi model
llm = ChatTongyi(
    model="qwen-vl-plus",
    temperature=0.2,
    api_key=os.environ["DASHSCOPE_API_KEY"]
)

search_tool =  TavilySearchResults(max_results=2)
tools = [search_tool]
# Tell the LLM which tools it can call
llm_with_tools = llm.bind_tools(tools)

# Define chatbot node
def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

# Define a Basic tool node
tool_node = ToolNode(tools=[search_tool])  


# Add chatbot node
graph_builder = StateGraph(State)
# The `tools_condition` function return "tools" if the chatbot ask to use a tool, and "END" if
# it is fine directly responding. This conditional routing define the main agent loop
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", tool_node)

# Add condition Edge
graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)

# Any time a tool is called, we return to the chatbot to decide the next step  # Fixed typo
graph_builder.add_edge("tools", "chatbot")
graph_builder.set_entry_point("chatbot")
memory = MemorySaver()
graph = graph_builder.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "3"}}
def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}, config):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)


while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        stream_graph_updates(user_input)
    except KeyboardInterrupt:  # Catch specific exception for graceful exit
        print("\nGoodbye!")
        break
    except Exception as e:  # Catch other exceptions and log them
        print(f"An error occurred: {e}")
        break

