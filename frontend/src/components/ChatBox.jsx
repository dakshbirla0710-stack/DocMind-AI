import { useEffect, useRef, useState } from "react";
import TypingIndicator from "./TypingIndicator";
import ReactMarkdown from "react-markdown";
function ChatBox({ messages, loading }) {
    const chatEndRef = useRef(null);
    const [copiedIndex, setCopiedIndex] = useState(null);
    useEffect(() => {
    chatEndRef.current?.scrollIntoView({
     behavior: "smooth",
     });
    }, [messages, loading]);
  if (messages.length === 0) return null;

 return (
  <div className="chat-box">

    {messages.map((msg, index) => (
      <div
        key={index}
        className={
          msg.type === "user"
            ? "user-message"
            : "ai-message"
        }
      >
        <strong>
          {msg.type === "user" ? "🧑 You" : "🤖 AI"}
        </strong>

      <ReactMarkdown>{msg.text}</ReactMarkdown>

    {msg.type === "ai" && (
    <button
        className="copy-btn"
        onClick={() => {
          navigator.clipboard.writeText(msg.text);
          setCopiedIndex(index);

          setTimeout(() => {
         setCopiedIndex(null);
       }, 2000);
    }}
  >
    {copiedIndex === index ? "✅ Copied" : "📋 Copy"}
  </button>
)}
      <div className="message-time">
        {msg.time}
      </div>

      </div>
    ))}

    {loading && <TypingIndicator />}

      <div ref={chatEndRef}></div>

    </div>
  );
}

export default ChatBox;