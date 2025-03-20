import React from 'react';
import { useLocation } from 'react-router-dom';
import axios from 'axios';

function ProductPage() {
    const location = useLocation();
    const { product } = location.state || {};
    
    const handleAddToCart = async () => {
        try {
            const response = await axios.put('/add_cart', {
                user_id: 1, 
                product_id: product.id,
                quantity: 1,
            });
            if (response.status === 200) {
                alert('Product added to cart!');
            }
        } catch (error) {
            console.error('Error adding to cart:', error);
            alert('Failed to add product to cart.');
        }
    };

    if (!product) {
        return <p>No product found</p>;
    }

    return (
        <section className="pro-page">
            <div className="prods">
                <img className="pro-img" src={product.img} alt="" />
                <div>
                    <h2 className="pro-title">{product.title}</h2>
                    <h2 className="pro-category">{product.category}</h2>
                    <h2 className="pro-descr">{product.description}</h2>
                    <button className="check" onClick={handleAddToCart}>
                        Add to Cart
                    </button>
                </div>
            </div>
        </section>
    );
}

export default ProductPage;
