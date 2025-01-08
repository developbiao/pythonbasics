from pathlib import Path
import sys
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

import os, getpass

# Add parent directory to Python path
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils.proxy_tool import ProxyTool

# Set and enable proxy
ProxyTool.set_proxy()
ProxyTool.enable_proxy()

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

_set_env("OPENAI_API_KEY")

gpt4o_chat = ChatOpenAI(model="gpt-4o", temperature=0.2)

# Create a message
msg = HumanMessage(content="Hello world", name="Biao")

# Message list
messages = [msg]


# Invoke the model with a list of messages
response = gpt4o_chat.invoke(messages)
print(response.content)
