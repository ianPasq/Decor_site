import NavBar from "./components/navbar.jsx";
import Footer from "./components/footer.jsx";
import Products from "./components/products.jsx";
import About from "./components/about.jsx";
import { useState } from 'react'
import './App.css'

function App() {
  

  return (
    <>
      <NavBar />
      <About /> 
      <Products />
      <Footer />
    </>
  )
}

export default App
