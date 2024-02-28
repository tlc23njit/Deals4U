import React from "react";

function Product({ product, style }) {
  return (
    <li className="Product" id={product.Product_ID} key={product.Product_ID} style={style}>
      <h3>{product.Product_Name}</h3>
      <a href={product.WebsiteUrl}>
        <img src={product.Image} alt={product.Product_Name} style={{ width: '100px', height: 'auto' }}/>
      </a>
      <h4 style={{ color: 'red' }}>ON SALE FOR : {product.Discount_Price}</h4>
      {product.Full_Price && product.Full_Price !== '' && (
        <h4>Originally : {product.Full_Price}</h4>
      )}
    </li>
  );
}

export default Product;
