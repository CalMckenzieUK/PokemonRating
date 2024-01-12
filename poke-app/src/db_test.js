import dotenv from 'dotenv'
import mysql from 'mysql2'

dotenv
  .config({
    path: '../.env'
  })


const DATABASE_URL = process.env.DATABASE_URL

const connection = mysql.createConnection(process.env.DATABASE_URL)
connection.query(
  'CREATE TABLE IF NOT EXISTS pokemon (id INTEGER PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255) NOT NULL, type VARCHAR(255) NOT NULL, img VARCHAR(255) NOT NULL)',
  function (err, results, fields) {
    if (err) {
      console.log(err.message)
    } else {
      console.log('Table created successfully!')   
    }
  }
)
console.log('Connected to PlanetScale!')
connection.end()