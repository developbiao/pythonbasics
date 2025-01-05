import sys
from pathlib import Path

# Add parent directory to Python path
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils.proxy_tool import ProxyTool
from pydantic_ai import Agent, RunContext
from pydantic_ai.settings import ModelSettings

# Set and enable proxy
ProxyTool.set_proxy()
ProxyTool.enable_proxy()


agent = Agent('gemini-1.5-flash', model_settings=ModelSettings(temperature=0.2))

async def main():
    result = await agent.run('What is the capital of France?')
    print(result.data)

    async with agent.run_stream('Introduction hangzhoou city') as response:
        print(await response.get_data())

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
