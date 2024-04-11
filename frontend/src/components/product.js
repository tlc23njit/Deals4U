import React from "react";
import { FaShoppingCart, FaTimes } from 'react-icons/fa'; // Import the shopping cart and times icons

function Product({ product, style, saveForLater, removeFromSaved }) {
  return (
    <li className="Product" id={product.product_id} style={style}>
      <h3>{product.product_name}</h3>
      <a href={product.websiteurl}>
        <img src={product.image} alt={product.product_name} style={{ width: '100px', height: 'auto' }}/>
      </a>
      <h4 style={{ color: 'red' }}>ON SALE FOR : {product.discount_price}</h4>
      {product.full_price && product.full_price !== '' && (
        <h4>Originally : {product.full_price}</h4>
      )}
      {saveForLater && (
        <button 
          onClick={() => saveForLater(product)}
          style={{ marginTop: '1rem', cursor: 'pointer', padding: '0.5rem 1rem', backgroundColor: '#4CAF50', color: 'white', border: 'none', borderRadius: '5px' }}
        >
          Save for Later <FaShoppingCart />
        </button>
      )}
      {removeFromSaved && (
        <button 
          onClick={() => removeFromSaved(product)}
          style={{ marginTop: '1rem', cursor: 'pointer', padding: '0.5rem 1rem', backgroundColor: '#ff6347', color: 'white', border: 'none', borderRadius: '5px' }}
        >
          Remove <FaTimes />
        </button>
      )}
    </li>
  );
}

export default Product;
