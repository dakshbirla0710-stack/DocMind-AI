# Embedding practice
# Stopped due to Google SDK/API compatibility issue.
# Will revisit during final RAG integration.
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="text-embedding-004",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

text = "Artificial Intelligence is changing the world."

vector = embeddings.embed_query(text)

print(vector)