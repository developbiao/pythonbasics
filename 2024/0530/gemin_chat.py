import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models
import os

# Set http proxy
os.environ["http_proxy"] = "http://127.0.0.1:8889"
os.environ["https_proxy"] = "http://127.0.0.1:8889"

project_id = "gen-lang-client-0115788367"
location = "us-central1"
# Set google application credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/gongbiao/Code/gemini/config/gen-lang-client-0115788367-a5e41245b79f.json"
vertexai.init(project=project_id, location=location)
print("google application credentials set:", os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
print("Vertex AI initialized")

# Load the Gemini 1.0 Pro model
model = GenerativeModel("gemini-1.0-pro")

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

# Generate text from text  prompts
model = GenerativeModel(
    "gemini-1.5-pro-001",
  )
responses = model.generate_content(
      ["Why is the sky blue?"],
      generation_config=generation_config,
      safety_settings=safety_settings,
      stream=True,
)

for response in responses:
    print(response.text, end="")
