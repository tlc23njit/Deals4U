import React, { useState, useEffect } from 'react';
import './banner.css';
import BannerLogo from '../images/bannerLogo.png';

const Banner = ({ message }) => {
  const [expiresIn, setExpiresIn] = useState(24 * 60 * 60);

  useEffect(() => {
    const intervalId = setInterval(() => {
      setExpiresIn((prevExpiresIn) => {
        if (prevExpiresIn === 0) {
          clearInterval(intervalId); 
          return 0;
        }
        return prevExpiresIn - 1;
      });
    }, 1000);
    return () => clearInterval(intervalId);
  }, []);

  useEffect(() => {
    const nextIntervalId = setTimeout(() => {
      setExpiresIn((prevExpiresIn) => prevExpiresIn - 1);
    }, 1000);
    return () => clearTimeout(nextIntervalId);
  }, [expiresIn]);
  


  const formatTime = (seconds) => {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const remainingSeconds = seconds % 60;
    return `${hours}h ${minutes}m ${remainingSeconds}s`;
  };

  return (
    <div className="banner">
      <img src= {BannerLogo} style={{width:'400px', float:'left', marginTop:'-60px'}}/>
      <h2 style={{color:'white',  fontSize:'20px' , marginLeft:'900px'}}>EXPIRES IN : {formatTime(expiresIn)}</h2>
    </div>
  );
};

export default Banner;