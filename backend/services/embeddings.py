from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-2",
    google_api_key=os.getenv("GEMINI_API_KEY")
)
def create_embeddings(chunks):

    vectors = embeddings.embed_documents(chunks)

    return vectors
def create_query_embedding(query):

    vector = embeddings.embed_query(query)

    return vector