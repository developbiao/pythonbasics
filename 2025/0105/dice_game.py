import sys
from pathlib import Path

# Add parent directory to Python path
project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils.proxy_tool import ProxyTool
from pydantic_ai import Agent, RunContext
from pydantic_ai.settings import ModelSettings
import random

# Set and enable proxy
ProxyTool.set_proxy()
ProxyTool.enable_proxy()


agent = Agent(
    'gemini-1.5-flash',
    deps_type=str,
    model_settings=ModelSettings(temperature=0.2),
    system_prompt = (
        "You're a dice game, you should roll the die and see if the number "
        "you get back matches the user's guess, if so, tell them they're a winner."
        "Use the player's name in the response."
    )
)

@agent.tool_plain
def roll_die() -> str:
    """
    Roll a six-sided die and return the result.
    """
    return str(random.randint(1, 6))

@agent.tool
def get_player_name(ctx: RunContext[str]) -> str:
    """
    Get the player's name
    """
    return ctx.deps


dice_result = agent.run_sync('My guess is 3', deps='BiaoGe')
print(dice_result.data)

