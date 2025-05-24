import { create } from 'zustand';
import axios from 'axios';
import { jwtDecode } from 'jwt-decode';

const API_URL = import.meta.env.VITE_API_URL;

const useAuthStore = create((set) => ({
  user: null,
  token: null,
  loading: false,
  error: null,

  login: async (email, password) => {
    set({ loading: true, error: null });
    try {
      const response = await axios.post(`${API_URL}/token`, {
        username: email,
        password,
        grant_type: 'password'
      });
      const token = response.data.access_token;
      const user = jwtDecode(token);
      localStorage.setItem('token', token);
      set({ user, token, loading: false });
    } catch (error) {
      set({ error: error.response?.data?.detail || 'Login failed', loading: false });
    }
  },

  logout: () => {
    localStorage.removeItem('token');
    set({ user: null, token: null });
  },

  initialize: () => {
    const token = localStorage.getItem('token');
    if (token) {
      const user = jwtDecode(token);
      set({ user, token });
    }
  }
}));

export default useAuthStore;
