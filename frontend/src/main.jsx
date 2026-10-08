import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './styles.css';

function App() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState('');
  const [downloadUrl, setDownloadUrl] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!file) {
      setStatus('Please choose a .blend file first.');
      return;
    }

    setIsLoading(true);
    setStatus('Uploading and rendering...');

    const formData = new FormData();
    formData.append('blend_file', file);

    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}/api/render`, {
        method: 'POST',
        body: formData,
      });

      const payload = await response.json();
      if (!response.ok) {
        throw new Error(payload.error || 'Render failed.');
      }

      setDownloadUrl(`${import.meta.env.VITE_API_URL || 'http://localhost:5000'}${payload.download_url}`);
      setStatus(`Render complete: ${payload.rendered_file}`);
    } catch (error) {
      setStatus(error.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app-shell">
      <div className="panel">
        <h1>Blender Online</h1>
        <p>Upload a Blender scene and render it in a headless Linux container.</p>

        <form onSubmit={handleSubmit}>
          <label className="upload-box">
            <input type="file" accept=".blend" onChange={(e) => setFile(e.target.files?.[0] || null)} />
            <span>{file ? file.name : 'Choose .blend file'}</span>
          </label>

          <button type="submit" disabled={isLoading || !file}>
            {isLoading ? 'Rendering...' : 'Render scene'}
          </button>
        </form>

        <div className="status">{status}</div>

        {downloadUrl && (
          <a className="download-link" href={downloadUrl} target="_blank" rel="noreferrer">
            Download rendered PNG
          </a>
        )}
      </div>
    </div>
  );
}

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>
);
