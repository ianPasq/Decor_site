import { useNavigate } from 'react-router-dom'


function Products() { 
    const navigate = useNavigate()
    const products = [
        {
            id: 1,
            img: "./assets/comfort-chair-and-table.avif",
            category: "Furniture",
            name: "Comfortable Dark Gray Chair and Table for Living Room",
            price: "$1000",
            description: " Add understated elegance to your living room with this cozy dark gray chair and matching table. The chair’s deep cushions and ergonomic design provide comfort and support, while the sturdy table, crafted from matching dark wood, offers a seamless, coordinated look. Perfect for lounging or entertaining, this set complements any casual or modern decor style."

        },
        {
            id: 2,
            img: "./assets/fancy-chair-and-table.avif",
            category: "Furniture",
            name: "Fancy Black and Gold Metal Chair and Glass Table",
            price: "$1500",
            description: " Elevate your space with this sophisticated black and gold chair paired with a sleek glass table. The chair’s frame boasts a glossy black finish with delicate golden accents, creating an air of luxury and modernity. Paired with a tempered glass table that shimmers with style, this set makes a statement in any room, ideal for those looking to add a touch of glamour to their home."
        },
        {
            id: 3,
            img: "./assets/living-room-chair.avif",
            category: "Furniture",
            name: "Wide Comfortable Gray Living Room Chair",
            price: "$300",
            description: " Sink into comfort with this generously sized gray living room chair, designed for lounging and relaxation. Its plush cushions and wide seating area invite you to curl up with a book or unwind after a long day. With a versatile shade of gray and a cozy, durable fabric, this chair is perfect for adding comfort and style to any living space."
        },
        {
            id: 4,
            img: "assets/minimalistic-chair-and-table-wood.avif",
            category: "Furniture",
            name: "Minimalistic Wooden Chair and Table",
            price: "$1200",
            description: " This sleek black and white office chair brings simplicity and style to your workspace. Its ergonomic design provides great support for long hours, while the minimalist color scheme effortlessly blends into any office environment. With adjustable height and a smooth swivel, this chair combines practicality with modern style for the perfect workspace addition."
        },
        {
            id: 5,
            img: "assets/lether-office-chair.avif",
            category: "Furniture",
            name: "Lether Office Chair",
            price: "$1200",
            description: " Add sophistication and comfort to your workspace with this rich brown leather office chair. Crafted from high-quality leather, it features plush padding and a supportive backrest, making it ideal for long hours at the desk. With adjustable height and a smooth swivel mechanism, this chair combines functionality with timeless style. The deep brown tone and elegant stitching add a touch of luxury, making it a perfect addition to any professional or home office setting."
        },
        {
            id: 6,
            img: "assets/minimalistic-metal-and-wood-chair.avif",
            category: "Furniture",
            name: "Minimal Black Metal and Wood Chair",
            price: "$1200",
            description: " A sleek fusion of metal and wood, this minimal chair combines industrial design with natural materials. The black metal frame provides durability, while the warm wooden seat adds an inviting touch. Perfect for a modern dining area, kitchen, or workspace, this chair brings a refined simplicity that complements any decor style."
        },
        {
            id: 7,
            img: "assets/white-simple-chair.avif",
            category: "Furniture",
            name: "Simple White Chair",
            price: "$1200",
            description: " Bring a touch of natural charm to your space with this simple white chair featuring a solid wooden stand. With a comfortable, contoured seat and a natural wood base, this chair fits beautifully in a dining room, bedroom, or any casual setting. Its clean, timeless look pairs well with any decor style, adding both function and elegance."
        },
        {
            id: 8,
            img: "assets/white-wooden-bed-table.avif",
            category: "Furniture",
            name: "Simple Small White Wooden bedside Table",
            price: "$1200",
            description: " This compact, white wooden bed table offers a practical solution for small spaces. With its simple design and lightweight build, it’s perfect for holding books, a lamp, or a morning cup of coffee. Place it next to your bed or sofa for convenient storage and a fresh, minimalist aesthetic."
        },
        {
            id: 9,
            img: "assets/yellow-chair.avif",
            category: "Furniture",
            name: "Alternative Minimal and Comfortable Yellow Chair",
            price: "$1500",
            description: " Brighten up any room with this unique, minimal yellow chair that blends comfort with bold style. Its soft, cushioned seat and relaxed design invite you to sit back, while the cheerful yellow hue adds a pop of color. Perfect for a modern living room, study, or bedroom, this chair offers an eye-catching alternative to traditional seating."
        }
        
    ];
    

    return (
        <section id="product1" className="sec-1">
            <h2>Featured Products</h2>
            <p>modern home design</p>

            <div className="pr1-cont">

                {products.map(product => (
                    <div className="cont" key={product.id}>
                        <img src={product.img} alt={product.name} />
                        <div className="desc">
                            <span>{product.category}</span>
                            <h5>{product.name}</h5>
                            <h4>{product.price}</h4>
                        </div>
                        <button className="check" onClick={()=>navigate('/product-page', { state: { product }})}>
                            Check
                        </button>
                        
                    </div>
                ))}

            </div>

        </section>
    ) 
}


export default Products
