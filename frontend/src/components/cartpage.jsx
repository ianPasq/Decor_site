import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CartPage = () => {
    axios.defaults.baseURL = 'http://localhost:3000';
    const [cartContents, setCartContents] = useState([]);
    const [errorMessage, setErrorMessage] = useState('');

    const fetchCart = async () => {
        try {
            const response = await axios.get('/view_cart', { 
                params: { user_id: 1 } 
            });
            
            setCartContents(response.data?.cart_contents || []);
        } catch (error) {
            console.error('Error:', error);
            setErrorMessage('Failed to fetch cart contents. Please try again later.');
            setCartContents([]); 
        }
    };

    useEffect(() => {
        fetchCart();
    }, []);

    const handleDeleteItem = async (productId) => {
        try {
            await axios.delete('/delete_cart', {
                data: {
                    user_id: 1,
                    product_id: productId,
                },
            });
            await fetchCart(); 
        } catch (error) {
            console.error('Error:', error);
            setErrorMessage('Failed to delete item from cart. Please try again later.');
        }
    };

    return (
        <div>
            <h2>Cart</h2>
            {errorMessage && <div className="error">{errorMessage}</div>}
            
            {cartContents.map((item) => (
                <li key={item.product_id}>
                    <img 
                        src={item.img} 
                        alt={item.name} 
                        style={{ width: '50px', height: '50px', objectFit: 'cover' }}
                    />
                    <div>{item.name}</div>
                    <div>Quantity: {item.quantity}</div>
                    <div>Price: ${item.price}</div>
                    <button onClick={() => handleDeleteItem(item.product_id)}>
                        Remove
                    </button>
                </li>
            ))}
            ) : (
                <p>Your cart is empty</p>
            )
        </div>
    );
};

export default CartPage;
