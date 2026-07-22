function QuestionSection({
    question,
    setQuestion,
    askPDF,
    uploaded,
    loading
}) {

    return (

        <>

    <div className="question-box">

        <textarea
             rows="3"
             placeholder="Ask anything about your PDF..."
             value={question}
             onChange={(e) => setQuestion(e.target.value)}
             onKeyDown={(e) => {
                if (e.key === "Enter" && !e.shiftKey) {
                e.preventDefault();
                askPDF();
         }
}}
         />

         <button
            onClick={askPDF}
            disabled={loading}
        >
            {loading ? "🤖 Thinking..." : "🚀 Ask AI"}
        </button>
    </div>
        </>

    );

}

export default QuestionSection;