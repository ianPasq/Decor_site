import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from "react-router-dom"


const LoginForm = () => {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  const navigate = useNavigate();
     
  const handleLogin = () => {
      if(email.length === 0){
        alert("Email was left Blank!");
      }
      else if(password.length === 0){
        alert("password was left Blank!");
      }
      else{
          axios.post('http://127.0.0.1:3000/login', {
              email: email,
              password: password
          })
          .then(function (response) {
              console.log(response);
              //console.log(response.data);
              navigate("/");
          })
          .catch(function (error) {
              console.log(error, 'error');
              if (error.response.status === 401) {
                  alert("Invalid credentials");

              }
      });
    }
  }

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
