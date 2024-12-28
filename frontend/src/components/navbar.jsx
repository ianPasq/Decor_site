import React from "react";


function NavBar() {
    return (
    <header>
        <nav>
            <div className="nav-btn">
                <a className="active" href="/">Home</a>
                <a href="/about">About</a>
                <a href="#category">Categories</a>
            </div>
            
            <div className="log">
                <a className="auth-btn" href="/login">Log-in</a>
                <a className="auth-btn" href="/register">Register</a>
            </div>
        </nav>

        <div className="top">
            <h1>Decorer</h1>
        </div>

    </header>
      
    )
  }
  
export default NavBar