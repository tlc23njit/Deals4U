const mysql = require('mysql2');
require('dotenv').config();

// Create a connection to the database
const dbConnection = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_DATABASE,
});

// Connect to the database
dbConnection.connect(error => {
  if (error) throw error;
  console.log("Successfully connected to the database.");
});

module.exports = dbConnection;
