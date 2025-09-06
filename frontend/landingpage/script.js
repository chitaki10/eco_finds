document.addEventListener('DOMContentLoaded', () => {
    // Select DOM elements
    const listProductBtn = document.getElementById('list-product-btn');
    const modal = document.getElementById('product-modal');
    const closeButton = document.querySelector('.close-button');
    const productForm = document.getElementById('product-form');
    const productShowcase = document.querySelector('.product-showcase .product-grid');

    // Sample products to start with
    const products = [
        { name: "Organic Honey", price: "25.00", image: "./img/honey.jpeg" },
        { name: "Herbal Tea Blend", price: "18.50", image: "https://via.placeholder.com/250x200.png?text=Herbal+Tea" },
        { name: "Natural Soap Bar", price: "8.99", image: "https://via.placeholder.com/250x200.png?text=Natural+Soap" },
        { name: "Eco-Friendly Water Bottle", price: "35.00", image: "https://via.placeholder.com/250x200.png?text=Water+Bottle" }
    ];

    // Function to render products
    function renderProducts() {
        productShowcase.innerHTML = ''; // Clear existing products
        products.forEach(product => {
            const productCard = document.createElement('div');
            productCard.classList.add('product-card');
            productCard.innerHTML = `
                <img src="${product.image}" alt="${product.name}">
                <h3>${product.name}</h3>
                <p class="price">$${product.price}</p>
                <button class="add-to-cart">Add to Cart</button>
            `;
            productShowcase.appendChild(productCard);
        });
    }

    // Call render function on page load
    renderProducts();

    // Show the modal when the user clicks the "List Your Product" button
    listProductBtn.addEventListener('click', () => {
        modal.style.display = 'block';
    });
    
    // Close the modal when the user clicks on the close button or outside the modal
    closeButton.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    window.addEventListener('click', (event) => {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });

    // Handle form submission to add a new product
    productForm.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent default form submission

        const productName = document.getElementById('product-name').value;
        const productPrice = parseFloat(document.getElementById('product-price').value).toFixed(2);
        const productImage = document.getElementById('product-image').value;

        // Create a new product object
        const newProduct = {
            name: productName,
            price: productPrice,
            image: productImage
        };

        // Add the new product to the array
        products.push(newProduct);

        // Re-render the product showcase to display the new product
        renderProducts();

        // Close the modal and reset the form
        modal.style.display = 'none';
        productForm.reset();
    });
});