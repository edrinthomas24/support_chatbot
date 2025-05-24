import { NavLink } from 'react-router-dom';
import useAuthStore from '../stores/authStore';

const Sidebar = () => {
  const { user, logout } = useAuthStore();

  return (
    <div className="sidebar">
      <div className="user-info">
        {user && (
          <>
            <p>Welcome, {user.name}</p>
            <button onClick={logout}>Logout</button>
          </>
        )}
      </div>
      <nav>
        <NavLink to="/" end>Chat</NavLink>
        {user?.is_admin && (
          <NavLink to="/knowledge">Knowledge Base</NavLink>
        )}
      </nav>
    </div>
  );
};

export default Sidebar;
