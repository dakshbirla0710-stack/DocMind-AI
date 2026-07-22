from services.embeddings import create_query_embedding

query = "What is Artificial Intelligence?"

vector = create_query_embedding(query)

print("Embedding Dimension:", len(vector))
print("First 10 values:", vector[:10])