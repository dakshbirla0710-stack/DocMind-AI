import faiss
import numpy as np

vectors = np.array([
    [1.0, 2.0],
    [2.0, 3.0],
    [3.0, 4.0],
    [8.0, 9.0]
], dtype='float32')

index = faiss.IndexFlatL2(2)

index.add(vectors)

print("Vectors stored successfully!")
query = np.array([[2.5, 3.5]], dtype='float32')

distances, indices = index.search(query, 2)

print("Distances:", distances)
print("Indices:", indices)