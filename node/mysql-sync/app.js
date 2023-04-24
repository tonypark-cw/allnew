let mysql = require('sync-mysql');

const env = require('dotenv').config({ path: './../../.env' });

let conn = new mysql({
   host: process.env.host,
   user: process.env.user,
   password: process.env.password,
   database: process.env.database,
});

let result = conn.query('select * from st_info;');
console.log(result);

let data = {
   st_id: '202399',
   name: 'Park',
   dept: 'Game',
};

let insertedId = data.st_id;
//select
result = conn.query('select * from st_info;');
console.log(result);

//delete
result = conn.query('delete from st_info where st_id = ?;', [insertedId]);
console.log(result);

//select
result = conn.query('select * from st_info;');
console.log(result);

//insert;
result = conn.query('insert into st_info values (?,?,?);', [data.st_id, data.name, data.dept]);
console.log(result);

//select
result = conn.query('select * from st_info;');
console.log(result);

//update
result = conn.query('update st_info set dept = ? where st_id = ?;', ['Game', insertedId]);
console.log(result);

//select
result = conn.query('select * from st_info;');
console.log(result);

//select query
result = conn.query('select * from st_info where st_id = ?;', [insertedId]);
console.log(result);
