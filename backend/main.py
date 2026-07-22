from fastapi import FastAPI,UploadFile,File
from pydantic import BaseModel
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
import google.generativeai as genai
import os
import shutil
import fitz
from services.pdf_loader import extract_text_from_pdf
from services.chunking import create_chunks
from services.embeddings import create_embeddings,create_query_embedding
from services.vector_store import create_vector_store, search_vector_store
from services.storage import save_vector_store, load_vector_store
from fastapi.middleware.cors import CORSMiddleware
# Load variables from .env
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create FastAPI app
app = FastAPI(
    title="DocMind AI",
    description="AI PDF Research Assistant",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

vector_index = None
stored_chunks = []

try:
    vector_index, stored_chunks = load_vector_store()
    print("Vector store loaded successfully!")
except:
    print("No saved vector store found.")

# Request Model
class PromptRequest(BaseModel):
    prompt: str
    history: List[dict] = []

# Home Route
@app.get("/")
def home():
    return {
        "message": "Welcome to DocMind AI 🚀"
    }

# AI Route
@app.post("/ask")
def ask_ai(data: PromptRequest):

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(data.prompt)

    return {
        "question": data.prompt,
        "answer": response.text
    }
@app.post("/upload-pdf")
def upload_pdf(file: UploadFile = File(...)):

    text = extract_text_from_pdf(file)

    chunks = create_chunks(text)

    vectors = create_embeddings(chunks)
    
    global vector_index, stored_chunks

    vector_index = create_vector_store(vectors)

    stored_chunks = chunks

    save_vector_store(vector_index, stored_chunks)

    return {
        "filename": file.filename,
        "total_chunks": len(chunks),
        "total_vectors": len(vectors),
        "embedding_dimension": len(vectors[0]),
        "first_chunk": chunks[0]
    }
#ask pdf
@app.post("/ask-pdf")
def ask_pdf(data: PromptRequest):

    global vector_index, stored_chunks

    query_vector = create_query_embedding(data.prompt)

    distances, indices = search_vector_store(
        vector_index,
        query_vector
    )

    relevant_chunks = []

    for i in indices[0]:
        relevant_chunks.append(stored_chunks[i])

    context = "\n\n".join(relevant_chunks)

    conversation = ""

    for msg in data.history:
        if msg["type"] == "user":
            conversation += f"User: {msg['text']}\n"
        else:
             conversation += f"AI: {msg['text']}\n"

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(
    f"""
    You are a helpful AI assistant answering questions about the uploaded PDF.

    Rules:
    - Always use the PDF context as your primary source.
    - Use the previous conversation to understand follow-up questions.
    - If the PDF contains enough information to make a reasonable suggestion or inference, you may do so.
    - If the answer truly cannot be determined from the PDF, clearly say so.

    Previous Conversation:
    {conversation}

    PDF Context:
    {context}

    Current Question:
    {data.prompt}
    """
)
    return {
        "answer": response.text
    }