from services.embeddings import create_embeddings
from services.vector_store import create_vector_store, search_vector_store

chunks = [
    "Cats are animals.",
    "Python is a programming language.",
    "The capital of India is New Delhi.",
    "Football is a popular sport."
]

# Create embeddings
vectors = create_embeddings(chunks)

# Store them in FAISS
index = create_vector_store(vectors)

# User question
query = "What is the capital of India?"

# Create embedding for the question
query_vector = create_embeddings([query])[0]

# Search
distances, indices = search_vector_store(index, query_vector)

print("Distances:", distances)
print("Indices:", indices)

print("\nMost Relevant Chunks:")
for i in indices[0]:
    print(chunks[i])