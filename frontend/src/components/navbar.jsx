import React, { useEffect, useState } from "react";
import { Link, useNavigate } from 'react-router-dom';


function NavBar() {
   
    const [isAuthenticated, setIsAuthenticated] = useState(false)
    const navigate = useNavigate()

    useEffect(() => {
      const token = localStorage.getItem("authToken");
      setIsAuthenticated(!!token);

    },[]);

    const handleLogout = () => {
      localStorage.removeItem('authToken');
      setIsAuthenticated(false);
      window.location.href = '/';
    };

    return (
     <header>
        <nav>
        {isAuthenticated ? (
          <>
           <div>

               <a className="user-btn" href="/profile"> Profile </a>
               <a className="user-btn" href="/cart"> Cart  </a>

            </div>
          </>
        ) : (
          <>
            <div className="nav-btn">
                <a className="active" href="/">Home</a>
                <a href="/about">About</a>
                <a href="#category">Categories</a>
            </div>

            <div className="log">
                <a className="auth-btn" href="/login">Log-in</a>
                <a className="auth-btn" href="/register">Register</a>
            </div>
          </>
        )} 
        </nav>

        <div className="top">
            <h1>Decorer</h1>
        </div>

     </header>
      
    )
  }
  
export default NavBar
