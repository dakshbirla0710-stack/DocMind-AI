from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Artificial Intelligence is changing the world very rapidly. Machine Learning is a subset of Artificial Intelligence that enables computers to learn from data without being explicitly programmed. Deep Learning is a branch of Machine Learning that uses neural networks with many layers. Natural Language Processing allows computers to understand and generate human language, while Computer Vision enables machines to analyze and interpret images and videos.
"""
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = text_splitter.split_text(text)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print("-" * 40)
    print(chunk)