# step 0. Imporint relevant Langchain libraries
import getpass
import os
from pathlib import Path
import sys
from langchain_community.adapters.openai import convert_openai_messages
from langchain_google_genai import ChatGoogleGenerativeAI

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

# step 1. instantiaing TavilyClient
from tavily import TavilyClient

_set_env("TAVILY_API_KEY")
client = TavilyClient()

# step 2. Executing the search query and getting the results
content = client.search("What happened in the latest beijing news?", search_depth="advanced")["results"]

query = "北京最近有什么大事件发生？"

# step 3. Setting up the prompts
prompt = [{
    "role": "system",
    "content":  f'You are an AI critical thinker research assistant. '\
                f'Your sole purpose is to write well written, critically acclaimed,'\
                f'objective and structured reports on given text.'
}, {
    "role": "user",
    "content": f'Information: """{content}"""\n\n' \
               f'Using the above information, answer the following'\
               f'query: "{query}" in a detailed report --'\
               f'Please use MLA format and markdown syntax.'\
               f'Please answer use chinese language.' 
}]


# step 4. Running the model through langchain
_set_env("GOOGLE_API_KEY")
lc_messages = convert_openai_messages(prompt)
report =  ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    max_tokens=512,
    timeout=None,
    max_retries=2
).invoke(lc_messages).content

# Step 5. Tha's it! Your search report is now done!
print(report)
