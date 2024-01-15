import dotenv from 'dotenv'
import mysql from 'mysql2'

function query (sql) {
const DATABASE_URL = process.env.DATABASE_URL;
dotenv.config({path: '../.env'});
const connection = mysql.createConnection(process.env.DATABASE_URL)
connection.query(
  sql,
  function (err, results, fields) {
    if (err) {
      console.log(err.message)
    } else {
      console.log('results: ', results)
      console.log('fields: ', fields)
    }
  }
)
console.log()
console.log('query done');
connection.end()
}

//function to return the results of a query as an json object
function queryJSON (sql) {
  const DATABASE_URL = process.env.DATABASE_URL;
  dotenv.config({path: '../.env'});
  const connection = mysql.createConnection(process.env.DATABASE_URL)
  connection.query(
    sql,
    function (err, results, fields) {
      if (err) {
        console.log(err.message)
      } else {
        console.log('results: ', results)
        console.log('fields: ', fields)
      }
    }
  )
  console.log()
  console.log('query done');
  connection.end()
  }


export { query };



// query('create table if not exists pokemon_rating (id int primary key auto_increment, left_pokemon_name varchar(255), right_pokemon_name varchar(255), who_won varchar(1), datetime_created datetime default current_timestamp)')
// query('insert into pokemon_rating (left_pokemon_name, right_pokemon_name, who_won) values ("'+oddish+'","'+gloom+'","'+who_won+'")')
// query('select count(*) from pokemon_rating');