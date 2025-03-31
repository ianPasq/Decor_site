import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from "react-router-dom"


const LoginForm = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault();

    if (email.trim() === '' || password.trim() === '') {
      alert('Email and Password cannot be empty!');
      return;
    }

    setLoading(true);

    try {
      const response = await axios.post('http://127.0.0.1:6000/login', {
        email,
        password,
      });

      if (response.status === 200) {
        const { token } = response.data;
        localStorage.setItem('authToken', token); 
        alert('Login successful!');
        window.location.href = '/'; 
      }
    } catch (error) {
      console.error(error);
      if (error.response && error.response.status === 401) {
        alert('Invalid credentials. Please try again.');
      } else {
        alert('An error occurred while logging in.');
      }
    } finally {
      setLoading(false);
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
