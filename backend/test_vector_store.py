from services.embeddings import create_embeddings
from services.vector_store import create_vector_store

chunks = [
    "Hello World",
    "This is a test."
]

vectors = create_embeddings(chunks)

index = create_vector_store(vectors)

print("Total vectors stored:", index.ntotal)