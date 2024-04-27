import NavBar from "./components/navbar.jsx";
import Footer from "./components/footer.jsx";
import Products from "./components/products.jsx";

import LoginForm from "./components/form.jsx";
import { useState } from 'react'
import './App.css'

function App() {
  

  return (
    <>
      <NavBar />
       
      <Products />
      <Footer />
      <LoginForm />
    </>
  )
}

export default App
