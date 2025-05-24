import { useState } from 'react';
import KnowledgeUpload from '../components/KnowledgeUpload';
import DocumentList from '../components/DocumentList';
import useAuthStore from '../stores/authStore';

const KnowledgePage = () => {
  const { user } = useAuthStore();
  const [refresh, setRefresh] = useState(false);

  if (!user?.is_admin) {
    return <div>Unauthorized access</div>;
  }

  return (
    <div className="knowledge-page">
      <h2>Knowledge Base Management</h2>
      <KnowledgeUpload onUpload={() => setRefresh(!refresh)} />
      <DocumentList refresh={refresh} />
    </div>
  );
};

export default KnowledgePage;
