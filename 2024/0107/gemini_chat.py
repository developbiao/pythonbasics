#!/usr/bin/env python3
import pathlib
import textwrap

import google.generativeai as genai

# Used to securely store your API key
#from google.colab import userdata

from IPython.display import display
from IPython.display import Markdown
import os


# Proxies
proxies = {
    "http": "http://127.0.0.1:8889",
    "https": "https://127.0.0.1:8889",
}

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
#GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')
# Config Google API Key
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

 # Model configuration
generation_config = { 
    "temperature": 0.9, 
    "top_p": 1, 
    "top_k": 1, 
    "max_output_tokens": 2048, 
} 


for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)


# Create model
#model = genai.GenerativeModel('gemini-pro', generation_config=generation_config)


# Send message question
#response = model.generate_content("What is the meaning of life?")

# Print response
#print(response)

