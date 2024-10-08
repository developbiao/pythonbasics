import os
from langchain_google_vertexai import ChatVertexAI

# [Optinal] set proxy
proxy = "http://127.0.0.1:8889"
os.environ["HTTP_PROXY"] = proxy
os.environ["HTTPS_PROXY"] = proxy
os.environ["http_proxy"] = proxy
os.environ["https_proxy"] = proxy

# load google access config file
credential_path="/Users/gongbiao/Code/vertex-ai/config/google_access_token_cp.json"
if os.path.exists(credential_path):
    print(f"the config load success")
else:
    print("config file does'not exists!")
    
# init vertex ai
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# Use chat mode
model = ChatVertexAI(model_name="gemini-1.5-pro-001", temperature=0)
response = model.invoke("Do you know chengdu?")
print(response.content)