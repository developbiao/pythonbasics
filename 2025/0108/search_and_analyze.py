import getpass
import os
from pathlib import Path
import sys
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import TavilySearchResults
import os

# Add parent directory to Python path
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

from utils.proxy_tool import ProxyTool

# Set and enable proxy
ProxyTool.set_proxy()
ProxyTool.enable_proxy()

# Set environment variables
_set_env("TAVILY_API_KEY")
_set_env("GOOGLE_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

