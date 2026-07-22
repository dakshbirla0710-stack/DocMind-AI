# 📄 DocMind AI

An AI-powered PDF chatbot that allows users to upload PDF documents and ask natural language questions. The application retrieves the most relevant sections from the document using vector search and generates accurate answers using Google's Gemini AI.

---

## 🚀 Features

- 📂 Upload PDF documents
- 🤖 Ask questions in natural language
- ⚡ Fast semantic search using FAISS
- 🧠 Google Gemini AI integration
- 💬 Chat-style interface
- 📝 Markdown response rendering
- 📋 One-click copy responses

---

## 🛠 Tech Stack

### Frontend
- React
- Axios
- React Markdown
- CSS

### Backend
- FastAPI
- Google Gemini API
- FAISS
- PyMuPDF
- LangChain Text Splitter

---

## ⚙️ How It Works

1. User uploads a PDF.
2. Text is extracted from the document.
3. The text is divided into smaller chunks.
4. Embeddings are generated for each chunk.
5. FAISS stores the vectors for fast retrieval.
6. When a question is asked:
   - The question is embedded.
   - Relevant chunks are retrieved.
   - Gemini generates an answer using only the retrieved context.

---

## 📂 Project Structure

```
DocMind-AI
│
├── backend
│   ├── services
│   ├── uploads
│   └── main.py
│
├── frontend
│   ├── src
│   └── components
│
└── requirements.txt
```

---

## 📸 Screenshots

(Add screenshots after deployment.)

---

## 👨‍💻 Author

Daksh Birla
