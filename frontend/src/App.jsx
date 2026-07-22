import { useState } from "react";
import axios from "axios";
import "./App.css";
import Header from "./components/Header";
import ChatBox from "./components/ChatBox";
import UploadSection from "./components/UploadSection";
import QuestionSection from "./components/QuestionSection";
import MainCard from "./components/MainCard";
function App() {
const [file, setFile] = useState(null);
const [question, setQuestion] = useState("");
const [messages, setMessages] = useState([]);
const [loading, setLoading] = useState(false);
const [uploaded, setUploaded] = useState(false);
const [error, setError] = useState("");
const uploadPDF = async () => {
const formData = new FormData();

  formData.append("file", file);

  const response = await axios.post(
    "http://127.0.0.1:8000/upload-pdf",   
    formData
  );

  console.log(response.data);
  setUploaded(true);

};
const askPDF = async () => {

  setError("");

  if (!uploaded) {
    setError("⚠️ Please upload a PDF first.");
    return;
  }

  if (!question.trim() || loading) return;

  setLoading(true);

  const response = await axios.post(
  "http://127.0.0.1:8000/ask-pdf",
  {
    prompt: question,
    history: messages,
  }
);
  
  setMessages((prev) => [
  ...prev,
  {
    type: "user",
    text: question,
    time: new Date().toLocaleTimeString([], {
      hour: "2-digit",
      minute: "2-digit",
    }),
  },
  {
      type: "ai",
     text: response.data.answer,
      time: new Date().toLocaleTimeString([], {
      hour: "2-digit",
      minute: "2-digit",
    }),
  },
]);

  setQuestion("");
  setLoading(false);
}

const clearChat = () => {
    setMessages([]);
    setQuestion("");
};

  return(
    <div className="container">

    <Header />

    {file && uploaded && (
      <div className="current-file">
      📄 Current PDF: <strong>{file.name}</strong>
      </div>
    )}

    <MainCard>

    <UploadSection
      file={file}
     setFile={setFile}
    uploadPDF={uploadPDF}
    uploaded={uploaded}
    />

    {error && (
      <div className="error-message">
     {error}
    </div>
  )}

<button onClick={clearChat}>
  🆕 New Chat 
</button>

<ChatBox
  messages={messages}
  loading={loading}
/>

<QuestionSection
  question={question}
  setQuestion={setQuestion}
  askPDF={askPDF}
  loading={loading}
  uploaded={uploaded}
/>

    </MainCard>

    </div>
  );
}

export default App;