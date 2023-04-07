let mysql = require('sync-mysql');

const env = require('dotenv').config({ path: './../../.env' });

let connection = new mysql({
   host: process.env.MYSQL_HOST,
   user: process.env.MYSQL_USER,
   port: process.env.MYSQL_PORT,
   password: process.env.MYSQL_PASSWD,
   database: process.env.MYSQL_DATABASE,
});

let result = connection.query('select * from st_info');
console.log(result);
