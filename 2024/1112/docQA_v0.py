# -*- encoding: utf-8 -*-

import os
import logging
from typing import List
from dotenv import load_dotenv
from dataclasses import dataclass
from langchain_google_vertexai import ChatVertexAI, VertexAIEmbeddings
from langchain.document_loaders.base import BaseLoader
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Qdrant
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.chains import RetrievalQA
from flask import Flask, request, render_template
import vertexai

# 配置类
@dataclass
class Config:
    PROJECT_ID: str = "gen-lang-client-0115788367"
    LOCATION: str = "us-central1"
    PROXY: str = "http://192.168.1.38:7897"
    CREDENTIAL_PATH: str = "/home/gongbiao/opt/config/google_access_token_cp.json"
    MODEL_NAME: str = "gemini-1.5-flash"
    EMBEDDING_MODEL: str = "text-embedding-004"
    CHUNK_SIZE: int = 200
    CHUNK_OVERLAP: int = 10
    TEMPERATURE: float = 0.2
    PORT: int = 5130

class DocumentProcessor:
    def __init__(self, base_dir: str):
        self.base_dir = base_dir
        self.documents = []
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP
        )

    def load_documents(self) -> List:
        file_handlers = {
            '.docx': Docx2txtLoader,
            '.pdf': PyPDFLoader,
            '.txt': TextLoader
        }

        for file in os.listdir(self.base_dir):
            file_path = os.path.join(self.base_dir, file)
            file_ext = os.path.splitext(file)[1]

            if file_ext in file_handlers:
                loader = file_handlers[file_ext](file_path)
                self.documents.extend(loader.load())

        return self.documents

    def split_documents(self):
        return self.text_splitter.split_documents(self.documents)

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

        # 设置代理
        for proxy_var in ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy']:
            os.environ[proxy_var] = Config.PROXY

        # 验证和设置凭证
        if not os.path.exists(Config.CREDENTIAL_PATH):
            raise FileNotFoundError("Google credentials file not found!")

        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Config.CREDENTIAL_PATH

        # 初始化Vertex AI
        vertexai.init(project=Config.PROJECT_ID, location=Config.LOCATION)
        self.logger.info("Vertex AI initialized successfully")

class QASystem:
    def __init__(self, chunked_documents):
        self.vectorstore = self.setup_vectorstore(chunked_documents)
        self.llm = self.setup_llm()
        self.qa_chain = self.setup_qa_chain()

    def setup_vectorstore(self, chunked_documents):
        return Qdrant.from_documents(
            documents=chunked_documents,
            embedding=VertexAIEmbeddings(model_name=Config.EMBEDDING_MODEL),
            #location=":memory:",
            location="192.168.1.66:6333",
            collection_name="my_documents"
        )

    def setup_llm(self):
        return ChatVertexAI(
            model_name=Config.MODEL_NAME,
            temperature=Config.TEMPERATURE
        )

    def setup_qa_chain(self):
        retriever = MultiQueryRetriever.from_llm(
            retriever=self.vectorstore.as_retriever(),
            llm=self.llm
        )
        return RetrievalQA.from_chain_type(self.llm, retriever=retriever)

    def get_answer(self, question: str):
        return self.qa_chain({"query": question})

def create_app(qa_system):
    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def home():
        if request.method == 'POST':
            question = request.form.get('question')
            result = qa_system.get_answer(question)
            return render_template('index.html', result=result)
        return render_template('index.html')

    return app

def main():
    # 初始化Vertex AI设置
    vertex_setup = VertexAISetup()

    # 处理文档
    doc_processor = DocumentProcessor('./OneFlower')
    documents = doc_processor.load_documents()
    chunked_documents = doc_processor.split_documents()

    # 设置QA系统
    qa_system = QASystem(chunked_documents)

    # 创建并运行Flask应用
    app = create_app(qa_system)
    app.run(host='0.0.0.0', debug=True, port=Config.PORT)

if __name__ == '__main__':
    main()