import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const RegisterForm = () => {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const registerUser = () => {
      axios.post('http://127.0.0.1:3000/sign_up', {
        name: name,
        email: email,
        password: password
      })
      .then(function (response) {
          console.log(response);
          navigate("/login");
      })
      .catch(function (error) {
          console.log(error, 'error');
          if (error.response.status === 401) {
              alert("Invalid credentials");
          }
          else { 
            alert("An error occurred.Please try again.")
          }
      });
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