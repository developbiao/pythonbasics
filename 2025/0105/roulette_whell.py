import sys
from pathlib import Path

# Add parent directory to Python path
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils.proxy_tool import ProxyTool
from pydantic_ai import Agent, RunContext

# Set and enable proxy
ProxyTool.set_proxy()
ProxyTool.enable_proxy()

roulette_agent = Agent(
    'gemini-1.5-flash',
    deps_type=int,
    result_type=bool,
    system_prompt = (
        'use the `roulette_wheel` function to see if the '
        'customer has won based on the number they provide.'
    ),

)

@roulette_agent.tool
async def roulette_whlee(ctx: RunContext[int], square: int) -> str:
    """
    Check if the square is a winner
    """
    return 'winner' if square == ctx.deps else 'loser'


# Run the agent
success_number = 18
result = roulette_agent.run_sync('Put my money on square eighteen', deps=success_number)
print(result.data)

result = roulette_agent.run_sync('I bet five is the winner', deps=success_number)
print(result.data)