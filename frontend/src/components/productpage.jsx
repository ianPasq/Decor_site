import { useLocation } from 'react-router-dom';

function ProductPage() {
    const location = useLocation();
    const { product } = location.state || {};
    
    if (!product) {
        return <p>No product found</p>;
    }

    return(
        <section className="pro-page">

            <div className="prods">
                <img className="pro-img" src= { product.img } alt="" />

                <div>
                    <h2 className="pro-title">{ product.title }</h2>
                    <h2 className="pro-category">{ product.category }</h2>
                    <h2 className="pro-descr">{ product.description }</h2>
                </div>
            </div>
        </section>
    )
}

export default ProductPage