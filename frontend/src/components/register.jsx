import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function RegisterForm() {
  const [name, setName]         = useState('');
  const [email, setEmail]       = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const registerUser = async () => {
    try {
      const res = await axios.post('/signup', { name, email, password });
      alert('Registration successful!');
      navigate('/login');
    } catch (err) {
      console.error(err);
      const status = err.response?.status;
      const msg    = err.response?.data?.error || err.message;

      if (status === 400) {
        alert(`Missing fields: ${msg}`);
      }
      else if (status === 409) {
        alert('Email already exists');
      }
      else {
        alert(`Signup failed: ${msg}`);
      }
    }
  };

    return (
      <div className='regis-section'>
        <div class="wrapper">
            <h2>Registration</h2>

            <form action="#">
                <div class="input-box">
                  <input type="text" value={name} onChange={(e) => setName(e.target.value)} placeholder="Enter your name" required></input>
                </div>

                <div class="input-box">
                  <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Enter your email" required></input>
                </div>

                <div class="input-box">
                  <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Create password" required></input>
                </div>

                <div class="input-box button">
                  <input type="button" onClick={() => registerUser()} value="Register Now"></input>
                </div>

                <div class="text">
                  <h3>Already have an account? <a href="/login">Login now</a></h3>
                </div>
                
            </form>
        </div>
      </div>        
    );

};


export default RegisterForm