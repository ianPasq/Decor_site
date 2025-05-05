import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from "react-router-dom"


function LoginForm() {
  const [email, setEmail]       = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async e => {
    e.preventDefault();
    if (!email || !password) {
      return alert('Email and password required');
    }

    try {
      await axios.post('/login', { email, password });
      alert('Login successful!');
      navigate('/');
    } catch (err) {
      console.error(err);
      const status = err.response?.status;
      const msg    = err.response?.data?.error || err.message;

      if (status === 401) {
        alert('Invalid credentials');
      } else {
        alert(`Login failed: ${msg}`);
      }
    }
  };
   

  return (
    <div className='login-form'>
      <div className='wrapper'>
        <div className='title-login'><span>Login</span></div>
      <form>
        <div className='row'>
          <label htmlFor="email">Email</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            id="form4email"
          />
        </div>

        <div className='row'>
          <label htmlFor="password">Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            id="form4password"
          />
        </div>

        <div class="pass"><a href="#">Forgot password?</a></div>
          <div class="row button">
            <input type="button" onClick={handleLogin} value="Login"></input>
          </div>
          <div class="signup-link">Not registered? <a href="/register">Register now!</a></div>
      </form>
      </div>
    </div>
  );
}


export default LoginForm;
