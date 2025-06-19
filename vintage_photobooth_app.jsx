import React, { useState, useRef } from "react";
import html2canvas from "html2canvas";
import "./App.css";

function App() {
  const [images, setImages] = useState([]);
  const [message, setMessage] = useState("");
  const previewRef = useRef(null);

  const handleUpload = (e) => {
    const files = Array.from(e.target.files).slice(0, 5);
    setImages(files.map((file) => URL.createObjectURL(file)));
  };

  const downloadImage = async () => {
    if (previewRef.current) {
      const canvas = await html2canvas(previewRef.current);
      const link = document.createElement("a");
      link.download = "polaroid_photos.png";
      link.href = canvas.toDataURL();
      link.click();
    }
  };

  return (
    <div className="min-h-screen bg-stone-100 p-8">
      <h1 className="text-3xl font-bold text-center mb-6">Vintage Polaroid Photobooth</h1>

      <div className="max-w-xl mx-auto space-y-4">
        <input
          type="file"
          accept="image/*"
          multiple
          onChange={handleUpload}
          className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-stone-200 file:text-stone-700 hover:file:bg-stone-300"
        />

        <input
          type="text"
          placeholder="Enter your custom message"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          className="block w-full border border-stone-400 p-2 rounded"
        />

        <div
          id="preview"
          ref={previewRef}
          className="flex flex-wrap justify-center gap-6 mt-6 bg-stone-50 p-4 rounded shadow-inner"
        >
          {images.map((src, index) => (
            <div
              key={index}
              className="w-48 h-64 bg-white rounded shadow-lg p-2 flex flex-col items-center justify-between"
            >
              <img
                src={src}
                alt="preview"
                className="w-full h-48 object-cover rounded filter sepia"
              />
              <p className="text-center text-xs mt-2 font-serif">{message}</p>
            </div>
          ))}
        </div>

        {images.length > 0 && (
          <button
            onClick={downloadImage}
            className="mt-4 px-6 py-2 bg-stone-700 text-white rounded hover:bg-stone-600"
          >
            Download Polaroid
          </button>
        )}
      </div>
    </div>
  );
}

export default App;
