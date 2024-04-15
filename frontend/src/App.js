import React, { useState, useEffect } from "react";
import Banner from './components/banner.js';
import Product from './components/product.js';

function App() {
  const [products, setProducts] = useState([]);
  const [savedProducts, setSavedProducts] = useState(() => {
    const savedProducts = localStorage.getItem('savedProducts');
    return savedProducts ? JSON.parse(savedProducts) : [];
  });
  const [showSavedProducts, setShowSavedProducts] = useState(false);
  const [selectedCategory, setSelectedCategory] = useState(null);
  const [theme, setTheme] = useState('light'); // State to store selected theme
  const [categories, setCategories] = useState([]); // State to store unique categories

  useEffect(() => {
    fetch("http://localhost:8000/products")
      .then((res) => res.json())
      .then((data) => {
        if (data.results) {
          setProducts(data.results.rows);
          const uniqueCategories = [...new Set(data.results.rows.map(product => product.category))];
          setCategories(uniqueCategories);
        } else {
          console.error('Error fetching products:', data);
        }
      })
      .catch((error) => {
        console.error('Error fetching products:', error);
      });
  }, []);

  useEffect(() => {
    localStorage.setItem('savedProducts', JSON.stringify(savedProducts));
  }, [savedProducts]);

  const saveForLater = (product) => {
    setSavedProducts((prevSavedProducts) => {
      if (!prevSavedProducts.find(p => p.product_id === product.product_id)) {
        return [...prevSavedProducts, product];
      }
      return prevSavedProducts;
    });
  };

  const removeFromSaved = (productToRemove) => {
    setSavedProducts((prevSavedProducts) => {
      return prevSavedProducts.filter(product => product.product_id !== productToRemove.product_id);
    });
  };

  const toggleSavedProducts = () => {
    setShowSavedProducts(!showSavedProducts);
  };

  const filterProductsByCategory = (category) => {
    setSelectedCategory(category);
  };

  const sortProductsByPrice = (direction) => {
    const sortedProducts = [...products].sort((a, b) => {
      const priceA = parseFloat((a.discount_price || '0').replace(/\$|,/g, ''));
      const priceB = parseFloat((b.discount_price || '0').replace(/\$|,/g, ''));
      if (direction === 'asc') {
        return priceA - priceB;
      } else {
        return priceB - priceA;
      }
    });
    setProducts(sortedProducts);
  };

  const toggleTheme = () => {
    setTheme(theme === 'light' ? 'dark' : 'light');
  };

  const productStyle = {
    padding: '0.5rem',
    paddingLeft: '1.5rem',
    paddingRight: '1.5rem',
    paddingBottom: '2rem',
    paddingTop: '2rem',
    backgroundColor: theme === 'light' ? '#e5e7eb' : '#333', // Update background color based on theme
    color: theme === 'light' ? '#333' : '#fff', // Update text color based on theme
    margin: '0.5rem',
    width: '16rem',
    listStyleType: 'none',
    textAlign: 'center'
  };

  const buttonStyle = {
    backgroundColor: theme === 'light' ? 'white' : '#333',
    color: theme === 'light' ? 'black' : 'white',
    border: theme === 'light' ? '1px solid black' : '1px solid white', 
    padding: '10px 20px',
    margin: '1rem',
    borderRadius: '5px',
    cursor: 'pointer'
  };

  return (
    <div className="App" style={{ backgroundColor: theme === 'light' ? '#fff' : '#111', color: theme === 'light' ? '#333' : '#fff' }}>
      <Banner/>
      <h1 style={{ textAlign: 'center' }}>🔥HOT DEALS🔥</h1>
      <div style={{ textAlign: 'center', marginBottom: '1rem' }}>
        <select onChange={(e) => filterProductsByCategory(e.target.value)}
          style={{
            padding: '8px',
            fontSize: '16px',
            borderRadius: '5px',
            cursor: 'pointer',
            outline: 'none',
            border: theme === 'light' ? '1px solid black' : '1px solid white',
            backgroundColor: theme === 'light' ? 'white' : '#333',
            color: theme === 'light' ? 'black' : 'white',
          }}
        >
          <option value="">All Categories</option>
          {categories.map(category => (
            <option key={category} value={category}>{category}</option>
          ))}
        </select>
      </div>

      <div style={{ textAlign: 'center', marginBottom: '1rem' }}>
        <select onChange={(e) => sortProductsByPrice(e.target.value)}
          style={{
            padding: '8px',
            fontSize: '16px',
            borderRadius: '5px',
            cursor: 'pointer',
            outline: 'none',
            border: theme === 'light' ? '1px solid black' : '1px solid white',
            backgroundColor: theme === 'light' ? 'white' : '#333',
            color: theme === 'light' ? 'black' : 'white',
          }}
        >
          <option value="">Sort by Price</option>
          <option value="asc">Price: Low to High</option>
          <option value="desc">Price: High to Low</option>
        </select>
      </div>

      <button onClick={toggleTheme} 
        style={buttonStyle}>
        Switch to {theme === 'light' ? 'Dark' : 'Light'} Theme
      </button>

      <button onClick={toggleSavedProducts} 
        style={buttonStyle}>
        Saved Products ({savedProducts.length})
      </button>

      {showSavedProducts ? (
        <>
          <h2 style={{ textAlign: 'center' }}>Saved for Later</h2>
          <ul style={{
            listStyleType: 'none',
            display: 'flex',
            justifyContent: 'center',
            flexWrap: 'wrap',
            padding: 0
          }}>
            {savedProducts.map((savedProduct) => (
              <Product key={savedProduct.product_id} product={savedProduct} style={productStyle} removeFromSaved={removeFromSaved} />
            ))}
          </ul>
        </>
      ) : (
        <ul style={{
          listStyleType: 'none',
          display: 'flex',
          justifyContent: 'center',
          flexWrap: 'wrap',
          padding: 0
        }}>
          {products
            .filter(product => !selectedCategory || product.category === selectedCategory)
            .map((product) => (
              <Product key={product.product_id} product={product} style={productStyle} saveForLater={saveForLater} /> // Update 'Product_ID' to 'product_id'
            ))}
        </ul>
      )}
    </div>
  );
}

export default App;
