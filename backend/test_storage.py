from services.embeddings import create_embeddings
from services.vector_store import create_vector_store
from services.storage import save_vector_store

chunks = [
    "Artificial Intelligence",
    "Machine Learning",
    "Deep Learning"
]

vectors = create_embeddings(chunks)

index = create_vector_store(vectors)

save_vector_store(index, chunks)

print("Files saved successfully!")