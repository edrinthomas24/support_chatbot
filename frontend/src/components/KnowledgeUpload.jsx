import { useState } from 'react';
import { uploadDocument } from '../api/chatService';
import useAuthStore from '../stores/authStore';

const KnowledgeUpload = () => {
  const [file, setFile] = useState(null);
  const [isUploading, setIsUploading] = useState(false);
  const [message, setMessage] = useState('');
  const { token } = useAuthStore();

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;
    
    setIsUploading(true);
    try {
      await uploadDocument(file, token);
      setMessage('Document uploaded successfully!');
      setFile(null);
    } catch (error) {
      setMessage('Error uploading document');
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <div className="upload-container">
      <h3>Upload Knowledge Document</h3>
      <form onSubmit={handleSubmit}>
        <input 
          type="file" 
          onChange={(e) => setFile(e.target.files[0])}
          accept=".pdf,.txt,.docx"
        />
        <button type="submit" disabled={!file || isUploading}>
          {isUploading ? 'Uploading...' : 'Upload'}
        </button>
      </form>
      {message && <p className="message">{message}</p>}
    </div>
  );
};

export default KnowledgeUpload;
