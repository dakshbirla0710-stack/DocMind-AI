import faiss
import pickle

def save_vector_store(index, chunks):

    faiss.write_index(index, "faiss_index.index")

    with open("chunks.pkl", "wb") as file:
        pickle.dump(chunks, file)
        
def load_vector_store():

    index = faiss.read_index("faiss_index.index")

    with open("chunks.pkl", "rb") as file:
        chunks = pickle.load(file)

    return index, chunks        