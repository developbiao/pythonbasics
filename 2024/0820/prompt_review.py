# -*- encoding: utf-8 -*-

import os
from langchain.prompts import PromptTemplate

template = """
你是一位专业的咖啡店创意文案撰写员。\n
对于售价为 {price} 元的 {coffee_name}咖啡，你需要写一篇文案，吸引更多的顾客。\n
"""

prompt = PromptTemplate.from_template(template)
prompt_str = prompt.format(price=20, coffee_name="生椰烘烤拿铁")

os.environ["MOONSHOT_API_KEY"] = os.getenv("OPENAI_API_KEY")
from langchain_community.chat_models.moonshot import MoonshotChat
from langchain_core.messages import HumanMessage

# Specific model name
chat = MoonshotChat(model="moonshot-v1-8k")

messages = [
    HumanMessage(content=prompt_str),
]

# Use streaming to get the response and print it
for chunk in chat.stream(messages):
    print(chunk.content, end="", flush=True)

