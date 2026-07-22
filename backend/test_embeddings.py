from services.embeddings import create_embeddings

chunks = [
    "Hello World",
    "This is a test."
]

vectors = create_embeddings(chunks)

print("Number of vectors:", len(vectors))
print("Dimension:", len(vectors[0]))