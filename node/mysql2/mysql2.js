const mysql = require('mysql2/promise');
const env = require('dotenv').config({ path: '../../.env' });

const db = async () => {
   try {
      let conn = await mysql.createConnection({
         host: process.env.host,
         user: process.env.user,
         password: process.env.password,
         database: process.env.database,
      });
      let [rows, fields] = await conn.query('select * from st_info;');
      console.log(rows);

      let data = {
         st_id: '202399',
         name: 'Park',
         dept: 'Game',
      };
      let insertedId = data.st_id;
      //delete row
      [rows, fields] = await conn.query('delete from st_info where st_id = ?;', [insertedId]);
      console.log(rows);

      //insert;
      let [results] = await conn.query('insert into st_info set ?', data);
      console.log(results);

      //select
      [rows, fields] = await conn.query('select * from st_info;');
      console.log(rows);

      //update
      [rows, fields] = await conn.query('update st_info set dept =? where st_id = ?;', ['Game', insertedId]);
      console.log(rows);

      //select
      [rows, fields] = await conn.query('select * from st_info;');
      console.log(rows);

      //select query
      [rows, fields] = await conn.query('select * from st_info where st_id =?;', [insertedId]);
      console.log(rows);
   } catch (error) {
      console.log('DB Connection Error : ');
      console.log(error);
   }
};
db();
