import React from "react";
import { FaShoppingCart, FaTimes } from 'react-icons/fa'; // Import the shopping cart and times icons

function Product({ product, style, saveForLater, removeFromSaved }) {
  return (
    <li className="Product" id={product.Product_ID} style={style}>
      <h3>{product.Product_Name}</h3>
      <a href={product.WebsiteUrl}>
        <img src={product.Image} alt={product.Product_Name} style={{ width: '100px', height: 'auto' }}/>
      </a>
      <h4 style={{ color: 'red' }}>ON SALE FOR : {product.Discount_Price}</h4>
      {product.Full_Price && product.Full_Price !== '' && (
        <h4>Originally : {product.Full_Price}</h4>
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
