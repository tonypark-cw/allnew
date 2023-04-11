const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const mysql = require('sync-mysql');
const env = require('dotenv').config({ path: '../.env' });

let connection = new mysql({
   host: process.env.host,
   user: process.env.user,
   password: process.env.password,
   database: process.env.database,
});

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get('/select', (req, res) => {
   const result = connection.query('select * from product;');
   // console.log(result);
   res.send(result);
});

app.get('/selectQuery', (req, res) => {
   const prodid = req.query.prodid;
   const result = connection.query('select * from product where prodid=?;', [prodid]);
   // console.log(result);
   res.send(result);
});

app.post('/insert', (req, res) => {
   const { prodid, prodname, prodprice, prodarti } = req.body;
   const result = connection.query('insert into product values (?, ?,?,?);', [prodid, prodname, prodprice, prodarti]);
   res.redirect('/selectQuery?prodid=' + prodid);
});

app.post('/update', (req, res) => {
   const { prodid, prodname, prodprice, prodarti } = req.body;
   const result = connection.query('update product set prodname=?, prodprice=?, prodarti=? where prodid=? ;', [
      prodname,
      prodprice,
      prodarti,
      prodid,
   ]);
   res.redirect('/selectQuery?prodid=' + prodid);
});

app.post('/delete', (req, res) => {
   const prodid = req.body.prodid;
   const result = connection.query('delete from product where prodid=?;', [prodid]);
   console.log(result);
   res.redirect('/select');
});

module.exports = app;
