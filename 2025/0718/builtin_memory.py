from agno.agent import Agent
from agno.models.openai import OpenAIChat
from rich.pretty import pprint

agent = Agent(
   model=OpenAIChat(id="gpt-4o") 
   # Set add_history_to_messages=true to add the previous hat history to the message sent to the Model.
)