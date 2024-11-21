import NavBar from "./components/navbar.jsx";
import Products from "./components/products.jsx";
import Footer from "./components/footer.jsx";
import LoginForm from "./components/login.jsx";
import RegisterForm from "./components/register.jsx";
import ProductPage from "./components/productpage.jsx" 
import CartPage from "./components/cartpage.jsx";
import { useState } from 'react'
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import './App.css'

function App() {
  

  return (
    <>
    <Router>
      <NavBar />
      <Routes>
          <Route path="/login" element={<LoginForm />} />
          <Route path="/register" element={<RegisterForm />} />
          <Route path="/product-page" element={<ProductPage />} />
          <Route exact path="/" element={<><Products/><Footer/></>}/>
      </Routes>
    </Router>

      
    </>
  )
}

export default App
