#  -*- encoding: utf-8 -*-

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vertex_ai import VertexAISetup, get_chat_model
from langchain_core.messages import HumanMessage, AIMessage

# =====================
if __name__ == '__main__':
    # Vertex AI初始化
    vertex_setup = VertexAISetup()
    model = get_chat_model()

    message = model.invoke([
        HumanMessage(content="Hi! I'm Biao"),
        AIMessage(content="Hello Biao! How can I assist you today?"),
        HumanMessage(content="What's my name?")
    ])
    print(message.content)



