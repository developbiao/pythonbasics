import os
import dotenv
import logging
from dataclasses import dataclass
from langchain_google_vertexai import ChatVertexAI
import vertexai
from langchain_google_vertexai import HarmCategory, HarmBlockThreshold
from langchain_core.messages import HumanMessage

# 配置类
@dataclass
class Config:
    PROJECT_ID: str
    LOCATION: str
    PROXY: str
    CREDENTIAL_PATH: str
    MODEL_NAME: str
    CHUNK_SIZE: int
    CHUNK_OVERLAP: int
    TEMPERATURE: float

    @staticmethod
    def from_env():
        dotenv.load_dotenv()
        return Config(
            PROJECT_ID=os.getenv("PROJECT_ID", "gen-lang-client-0115788367"),
            LOCATION=os.getenv("LOCATION", "us-central1"),
            PROXY=os.getenv("PROXY", "http://127.0.0.1:7897"),
            CREDENTIAL_PATH=os.getenv("CREDENTIAL_PATH", "/Users/gongbiao/Code/vertex-ai/config/google_access_token_cp.json"),
            MODEL_NAME=os.getenv("MODEL_NAME", "gemini-1.5-flash"),
            CHUNK_SIZE=int(os.getenv("CHUNK_SIZE", 200)),
            CHUNK_OVERLAP=int(os.getenv("CHUNK_OVERLAP", 10)),
            TEMPERATURE=float(os.getenv("TEMPERATURE", 0.2))
        )


class VertexAISetup:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.setup_logging()
        self.config = Config.from_env()
        self.setup_environment()

    @staticmethod
    def setup_logging():
        logging.basicConfig(level=logging.DEBUG)

    def setup_environment(self):
        for proxy_var in ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy']:
            os.environ[proxy_var] = self.config.PROXY

        if not os.path.exists(self.config.CREDENTIAL_PATH):
            raise FileNotFoundError("Google credentials file not found!")

        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.config.CREDENTIAL_PATH

        vertexai.init(project=self.config.PROJECT_ID, location=self.config.LOCATION)
        self.logger.info("Vertex AI initialized successfully")

def get_chat_model():
    config = Config.from_env()
    safety_settings = {
        HarmCategory.HARM_CATEGORY_UNSPECIFIED: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
    }
    return ChatVertexAI(
        model_name=config.MODEL_NAME,
        temperature=config.TEMPERATURE,
        safety_settings=safety_settings
    )
