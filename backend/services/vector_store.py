import faiss
import numpy as np

def create_vector_store(vectors):

    dimension = len(vectors[0])

    index = faiss.IndexFlatL2(dimension)

    vectors = np.array(vectors).astype("float32")

    index.add(vectors)

    return index
def search_vector_store(index, query_vector, k=3):

    query_vector = np.array([query_vector]).astype("float32")

    distances, indices = index.search(query_vector, k)

    return distances, indices