import sys
from pathlib import Path

# Add parent directory to Python path
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils.proxy_tool import ProxyTool
from pydantic_ai import Agent

# Set and enable proxy
ProxyTool.set_proxy()
ProxyTool.enable_proxy()

agent = Agent(
    'gemini-1.5-flash',
    system_prompt = 'Be concise, reply with one sentence.',
)

result = agent.run_sync('Where does "golang" come from?')
print(result.data)

# Optionally disable proxy when done
ProxyTool.disable_proxy()
