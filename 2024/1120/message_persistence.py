
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vertex_ai import VertexAISetup, get_chat_model
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

# =====================
if __name__ == '__main__':
    # Vertex AI初始化
    vertex_setup = VertexAISetup()
    model = get_chat_model()

    # Define a new graph
    workflow = StateGraph(state_schema=MessagesState)

    # Define the functions that calls the model
    def call_model(state: MessagesState):
        response = model.invoke(state["messages"])
        return {"messages": response}


    # Define the (single) node in the graph
    workflow.add_edge(START, "model")
    workflow.add_node("model", call_model)

    # Add memory
    memory = MemorySaver()
    app = workflow.compile(checkpointer=memory)

    config = {"configurable": {"thread_id": "abc123"}}
    query = "Hi! I'm Biao." 
    input_messages = [HumanMessage(query)]
    output = app.invoke({"messages": input_messages}, config=config)
    output["messages"][-1].pretty_print() # output contains all messges in state

    qeury = "What's my name?"

    input_messages = [HumanMessage(query)]
    output = app.invoke({"messages": input_messages}, config=config)
    output["messages"][-1].pretty_print()
