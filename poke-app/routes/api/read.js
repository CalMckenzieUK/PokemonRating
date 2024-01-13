import { mysqlconnFn } from '/poke-app/lib/server/db/mysql.js';

export async function get() {

    let mysqlconn = await mysqlconnFn();

    let results = await mysqlconn.query('show columns from pokemon_rating')
        .then(function([rows,fields]) {
            console.log(rows);
            return rows;
        });
    
    return {
        body: results
    }
}