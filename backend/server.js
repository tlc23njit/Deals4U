const express = require('express');
const cors = require('cors');
const dbConnection = require('./dbconnection'); // Adjust the path as necessary


const app = express();

app.use(cors());
app.use(express.json()); // Middleware for parsing application/json


app.get('/products', (req, res) => {  
  dbConnection.query('SELECT * FROM Products', (err, results) => {
      if (err) {
          console.error('Error fetching products:', err);
          res.status(500).send('Error fetching products');
          return;
      }
      res.json({results});
  });
});


app.listen(8000, () => {
  console.log(`Server is running on port 8000.`);
});


