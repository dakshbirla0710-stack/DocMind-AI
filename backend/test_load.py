from services.storage import load_vector_store

index, chunks = load_vector_store()

print("Vectors Loaded:", index.ntotal)

print("\nChunks Loaded:")

for chunk in chunks:
    print("-", chunk)