import React, { useState } from 'react';
import './styles.css';

function App() {
  const [file, setFile] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [downloadUrl, setDownloadUrl] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

    setIsLoading(true);
    const formData = new FormData();
    formData.append('video', file);

    try {
      const response = await fetch('http://localhost:8000/create_clips', {
        method: 'POST',
        body: formData,
      });
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      setDownloadUrl(url);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Video Clipper</h1>
      <form onSubmit={handleSubmit}>
        <input 
          type="file" 
          accept="video/*" 
          onChange={(e) => setFile(e.target.files[0])} 
        />
        <button type="submit" disabled={!file || isLoading}>
          {isLoading ? 'Processing...' : 'Generate Clips'}
        </button>
      </form>
      {downloadUrl && (
        <a href={downloadUrl} download="clips.zip">
          Download Clips
        </a>
      )}
    </div>
  );
}

export default App;