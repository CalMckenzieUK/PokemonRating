import mysql from "mysql2";
import dotenv from "dotenv";

const conn = mysql.createConnection(process.env.DATABASE_URL)


conn.connect(function(err) {
  if (err) throw err;
  console.log("Succesfully connected to PlanetScale!");
  process.exit(0)
});