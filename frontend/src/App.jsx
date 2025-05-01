import React, { useState } from "react";
import NavBar from "./components/navbar.jsx";
import Products from "./components/products.jsx";
import Footer from "./components/footer.jsx";
import LoginForm from "./components/login.jsx";
import RegisterForm from "./components/register.jsx";
import ProductPage from "./components/productpage.jsx";
import CartPage from "./components/cartpage.jsx";
import Profile from "./components/account.jsx"
import { BrowserRouter as Router, Routes, Route, } from "react-router-dom";
import './App.css'



function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(!!localStorage.getItem("authToken")); 
  
  const handleLogin = (token) => {
    localStorage.setItem("authToken", token);
    setIsAuthenticated(true);
  };

  const handleLogout = () => {
    localStorage.removeItem("authToken");
    setIsAuthenticated(false);
  }

  return (
    <>
    <Router>

      <NavBar isAuthenticated={isAuthenticated} handleLogout={handleLogout} />

      <Routes>

          <Route path="/login" element={<LoginForm onLogin={handleLogin} />} />

          <Route path="/register" element={<RegisterForm />} />

          <Route path="/profile" element={isAuthenticated ? <Profile /> : <LoginForm />} />

          <Route path="/cart" element={isAuthenticated ? <CartPage /> : <LoginForm />} />

          <Route path="/product-page" element={<ProductPage />} />

          <Route exact path="/" element={<><Products/><Footer/></>}/>
          
      </Routes>

    </Router>

      
    </>
  )
}

export default App
