function AnswerBox({ answer, loading }) {

  if (!answer && !loading) return null;

  return (
    <div className="answer-box">

      <div className="answer-header">
        🤖 <span>DocMind AI</span>
      </div>

      <div className="answer-content">
        {loading ? (
          <p>Thinking...</p>
        ) : (
          <p>{answer}</p>
        )}
      </div>
    </div>
  );
}

export default AnswerBox;