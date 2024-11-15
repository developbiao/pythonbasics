# -*- encoding: utf-8 -*-

import os
import logging
from typing import List
from dotenv import load_dotenv
from dataclasses import dataclass
from langchain_google_vertexai import ChatVertexAI
import vertexai
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate
)
from langchain_google_vertexai import HarmCategory, HarmBlockThreshold

# 配置类
@dataclass
class Config:
    PROJECT_ID: str = "gen-lang-client-0115788367"
    LOCATION: str = "us-central1"
    PROXY: str = "http://192.168.1.41:7897"
    CREDENTIAL_PATH: str = "/home/gongbiao/opt/config/google_access_token_cp.json"
    MODEL_NAME: str = "gemini-1.5-flash"
    EMBEDDING_MODEL: str = "text-embedding-004"
    CHUNK_SIZE: int = 200
    CHUNK_OVERLAP: int = 10
    TEMPERATURE: float = 0.2
    PORT: int = 5130


class VertexAISetup:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.setup_logging()
        self.setup_environment()

    @staticmethod
    def setup_logging():
        logging.basicConfig(level=logging.DEBUG)

    def setup_environment(self):
        load_dotenv()

        for proxy_var in ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy']:
            os.environ[proxy_var] = Config.PROXY

        if not os.path.exists(Config.CREDENTIAL_PATH):
            raise FileNotFoundError("Google credentials file not found!")

        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Config.CREDENTIAL_PATH

        vertexai.init(project=Config.PROJECT_ID, location=Config.LOCATION)
        self.logger.info("Vertex AI initialized successfully")


if __name__ == '__main__':
    #Vertex AI初始化
    vertex_setup = VertexAISetup()
            # Safety settings for content
    safety_settings = {
            HarmCategory.HARM_CATEGORY_UNSPECIFIED: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
    }
    llm = ChatVertexAI(
        model_name=Config.MODEL_NAME,
        temperature=Config.TEMPERATURE,
        safety_settings=safety_settings
    )

    # 设定 AI 的角色和目标
    role_template = "你是一个为花店电商公司工作的AI助手,你的目标 是帮助客户根据他们的喜好做出明智的鲜花购买决策"

    # COT的duqv部分， AI解释推理过程并加入一些先前的对话示例 (Few-Shot Leanring)
    # COT 的模板
    cot_template = """
    作为一个为花店电商公司工作的AI助手，我的目标是帮助客户根据他们的喜好做出明智的决定。

我会按部就班的思考，先理解客户的需求，然后考虑各种鲜花的涵义，最后根据这个需求，给出我的推荐。
同时，我也会向客户解释我这样推荐的原因。

示例 1:
  人类：我想找一种象征爱情的花。
  AI：首先，我理解你正在寻找一种可以象征爱情的花。在许多文化中，红玫瑰被视为爱情的象征，这是因为它们的红色通常与热情和浓烈的感情联系在一起。因此，考虑到这一点，我会推荐红玫瑰。红玫瑰不仅能够象征爱情，同时也可以传达出强烈的感情，这是你在寻找的。

示例 2:
  人类：我想要一些独特和奇特的花。
  AI：从你的需求中，我理解你想要的是独一无二和引人注目的花朵。兰花是一种非常独特并且颜色鲜艳的花，它们在世界上的许多地方都被视为奢侈品和美的象征。因此，我建议你考虑兰花。选择兰花可以满足你对独特和奇特的要求，而且，兰花的美丽和它们所代表的力量和奢侈也可能会吸引你。

    """

    system_prompt_role = SystemMessagePromptTemplate.from_template(role_template)
    system_prompt_cot = SystemMessagePromptTemplate.from_template(cot_template)

    # User question
    human_template = "{human_input}"
    human_prompt = HumanMessagePromptTemplate.from_template(human_template)

    # 将上所有信息结合为一个聊天 prompt
    chat_prompt = ChatPromptTemplate.from_messages([system_prompt_role, system_prompt_cot, human_prompt])

    prompt = chat_prompt.format_prompt(human_input="我想为我的情人购买一些花。她喜欢粉色和紫色，你有什么好的建议吗？").to_messages()

    # Receive the response
    response = llm.invoke(prompt)

    # Print the response message
    print("-------- Reply message-------")
    print(response.content)




