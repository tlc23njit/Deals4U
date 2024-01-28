import React from 'react';
import './banner.css';
import BannerLogo from '../images/bannerLogo.png';

const Banner = ({ message }) => {
  return (
    <div className="banner">
      <img src= {BannerLogo} style={{width:'400px', float:'left', marginTop:'-60px'}}/>
      <h2 style={{color:'white',  fontSize:'20px' , marginLeft:'1000'}}>EXPIRES IN : </h2>
    </div>
  );
};

export default Banner;