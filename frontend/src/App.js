import React, { useState, useEffect } from "react";
import Banner from './components/banner.js';
import Product from './components/product.js';

function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/products")
      .then((res) => res.json())
      .then((data) => {
        if (data.results) {
          setProducts(data.results);
        } else {
          console.error('Error fetching products:', data);
        }
      })
      .catch((error) => {
        console.error('Error fetching products:', error);
      });
  }, []);

  const productStyle = {
    padding: '0.5rem',
    paddingLeft: '1.5rem',
    paddingRight: '1.5rem',
    paddingBottom: '2rem',
    paddingTop: '2rem',
    backgroundColor: '#e5e7eb',
    margin: '0.5rem',
    width: '16rem', // Adjusted for a bigger size
    listStyleType: 'none', // Remove bullet points
    textAlign: 'center' // Center text inside the product
  };

  return (
    <div className="App">
      <Banner/>
      <h1 style={{ textAlign: 'center' }}>🔥HOT DEALS🔥</h1>
      <ul style={{
        listStyleType: 'none', // Remove bullet points
        display: 'flex', // Use flexbox for horizontal alignment
        justifyContent: 'center', // Center items horizontally
        flexWrap: 'wrap', // Allow items to wrap in the container
        padding: 0 // Remove padding to align properly
      }}>
        {products.map((product) => (
          <Product key={product.Product_ID} product={product} style={productStyle} />
        ))}
      </ul>
    </div>
  );
}

export default App;