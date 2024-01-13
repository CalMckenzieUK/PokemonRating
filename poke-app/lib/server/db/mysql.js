
import mysql from 'mysql2/promise';

let mysqlconn = null;

export function mysqlconnFn() { 
    if (!mysqlconn) {
        const connection = mysql.createConnection(process.env.DATABASE_URL)
    };
    return mysqlconn;
}