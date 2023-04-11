const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const mysql = require('sync-mysql');
const env = require('dotenv').config({ path: '../../.env' });

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

app.get('/hello', (req, res) => {
   res.send('Veni! Vidi! Vici!');
});

app.get('/select', (req, res) => {
   const result = connection.query('select * from user;');
   console.log(result);
   res.send(result);
});

app.post('/select', (req, res) => {
   const result = connection.query('select * from user;');
   console.log(result);
   res.send(result);
});

app.get('/selectQuery', (req, res) => {
   const userid = req.query.userid;
   console.log(typeof userid);
   const result = connection.query('select * from user where userid=?;', [userid]);
   console.log(result);
   res.send(result);
});

app.post('/selectQuery', (req, res) => {
   const userid = req.body.userid;
   console.log(typeof userid);
   const result = connection.query('select * from user where userid=?;', [userid]);
   console.log(result);
   res.send(result);
});

module.exports = app;
