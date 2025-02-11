import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CartPage = () => {
  const [cartContents, setCartContents] = useState([]);
  const [errorMessage, setErrorMessage] = useState('');


  const fetchCart = async () => {
    try {
      const response = await fetch.get('/view_cart?user_id=1');
      if (!response.ok) {
        throw new Error('failed to fetch cart');
      }
      const data = await response.json();
      setCartContents(data.cart_contents);
    } catch (error) {
      console.error('Error:', error);
      setErrorMessage('Failed to fetch cart contents. Please try again later.');
    }
  };

  useEffect(() => {
    fetchCart();
  },[]);

  const handleDeleteItem = async (productId) => {
    try {
      await axios.delete('/delete_cart', {
        data: {
          user_id: 1, 
          product_id: productId,
        },
      });
      fetchCart();
    } catch (error) {
      console.error('Error:', error);
      setErrorMessage('Failed to delete item from cart. Please try again later.');
    }
  };

  return (
    <div>
      <h2>Cart</h2>
      {errorMessage && <div>{errorMessage}</div>}
      <ul>
        {cartContents.map((item) => (
          <li key={item.product_id}>
            <div>{item.name}</div>
            <div>Quantity: {item.quantity}</div>
            <div>Price: ${item.price}</div>
            <button onClick={() => handleDeleteItem(item.product_id)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CartPage;
