const { Client } = require('pg');
require('dotenv').config();

// Create a connection to the database
const dbConnection = new Client({
  connectionString : process.env.DB_SSL,
  ssl: {
    rejectUnauthorized: false
  }
})

// Connect to the database
dbConnection.connect()
  .then(() => console.log("Successfully connected to the database."))
  .catch(error => console.error('Error connecting to database:', error.stack));

module.exports = dbConnection;
