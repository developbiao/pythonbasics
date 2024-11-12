# -*- encoding: utf-8 -*-

import os
from dotenv import load_dotenv
from langchain_google_vertexai import ChatVertexAI
import json

load_dotenv() # load .env file environment

# init environemnt
proxy = "http://192.168.1.38:7897"
os.environ["HTTP_PROXY"] = proxy
os.environ["HTTPS_PROXY"] = proxy
os.environ["http_proxy"] = proxy
os.environ["https_proxy"] = proxy

# load google access config file
credential_path=os.path.expanduser("/home/gongbiao/opt/config/google_access_token_cp.json")
if os.path.exists(credential_path):
    print(f"the config load success")
else:
    print("config file does'not exists!")

# init vertex ai
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


PROJECT_ID = "gen-lang-client-0115788367"
LOCATION = "us-central1"
import vertexai

vertexai.init(project=PROJECT_ID, location=LOCATION)

# Import document loader
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader

# 1. Load Documents
base_dir = './OneFlower'

print("#A0001")

documents = []
for file in os.listdir(base_dir):
    # Build full file path
    file_path = os.path.join(base_dir, file)
    if file.endswith('.docx'):
        loader = Docx2txtLoader(file_path)
        documents.extend(loader.load())
    if file.endswith('.pdf'):
        loader = PyPDFLoader(file_path)
        documents.extend(loader.load())
    if file.endswith('.txt'):
        loader = TextLoader(file_path)
        documents.extend(loader.load())

# 2. Split Documents to chunk save to vertex database
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_spliter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=10)
chunked_documents = text_spliter.split_documents(documents)
print("#A0002")

# 3. Store chunk data to vertex database Qdrant
from langchain_community.vectorstores import Qdrant
from langchain_google_vertexai import VertexAIEmbeddings
import logging

# Setting Logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Initializing Qdrant vectorstore...")

vectorstore = Qdrant.from_documents(
    documents=chunked_documents,
    embedding=VertexAIEmbeddings(model_name="text-embedding-004"),
    location=":memory:",
    collection_name="my_documents", # Specify collection name
)

logger.debug("Qdrant vectorstore initialized successfully.")

print("#001")

# 4. Retrieval prepare for LLM
import logging
from langchain.retrievers.multi_query import MultiQueryRetriever # MultiQueryRetriever tool
from langchain.chains import RetrievalQA

# Setting Logging
logging.basicConfig()
logging.getLogger('langchain.retrievers.multi_query').setLevel(logging.INFO)
#os.environ["MOONSHOT_API_KEY"] = os.getenv("OPENAI_API_KEY")

# # New chat model
# llm = MoonshotChat(model="moonshot-v1-128k")
# Use chat mode
llm = ChatVertexAI(
    model_name="gemini-1.5-flash",
    temperature=0.2,
)

# New MultiQueryRetriever
retriever_from_llm = MultiQueryRetriever.from_llm(retriever=vectorstore.as_retriever(), llm=llm)

# New RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever_from_llm)

print("#002")

# 5. Output QA UI implement
from flask import Flask, json, request, render_template
app = Flask(__name__) # Flask App

print("#003")

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Received question
        question = request.form.get('question')

        # RetrievalQA chain - Read question and generate answer
        result = qa_chain({"query": question})

        # Render result for page
        return render_template('index.html', result=result)
    return render_template('index.html')

print("#004")
if __name__ == '__main__':
    print("#005")
    print("Start running server...")
    app.run(host='0.0.0.0', debug=True, port=5130)
