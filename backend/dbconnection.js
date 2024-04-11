const { Client } = require('pg');
require('dotenv').config();

// Create a connection to the database
const dbConnection = new Client({
  user: process.env.DB_USER,
  host: process.env.DB_HOST,
  database: process.env.DB_DATABASE,
  password: process.env.DB_PASSWORD,
  port: process.env.DB_PORT,
});

// Connect to the database
dbConnection.connect()
  .then(() => console.log("Successfully connected to the database."))
  .catch(error => console.error('Error connecting to database:', error.stack));

module.exports = dbConnection;
