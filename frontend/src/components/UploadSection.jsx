import { useRef } from "react";
function UploadSection({
    file,
    setFile,
    uploadPDF,
    uploaded
}) {

  const inputRef = useRef(null);
   return (
  <div className="upload-section">

    <div
      className="upload-box"
      onClick={() => inputRef.current.click()}
      onDragOver={(e) => e.preventDefault()}
     onDrop={(e) => {
     e.preventDefault();
      setFile(e.dataTransfer.files[0]);
  }}
>
      <div className="upload-icon">
        📄
      </div>

      <h2>Upload your PDF</h2>

      <p>
        Drag & Drop or Click Below
      </p>

    <input
        ref={inputRef}
        type="file"
        accept=".pdf"
        style={{ display: "none" }}
        onChange={(e) => setFile(e.target.files[0])}
    />
    {file && (
      <p className="selected-file">
      Selected:
      <strong> {file.name}</strong>
      </p>
    )}

    </div>
    <button
       onClick={uploadPDF}
       disabled={uploaded}
    >
       {uploaded ? "✅ Uploaded" : "📤 Upload PDF"}
    </button>
    </div>
    );
}

export default UploadSection;