const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const mysql = require('sync-mysql');
const env = require('dotenv').config({ path: '../../.env' });

function makeResultTemplate(body) {
   let result = `
   <!doctype html>
   <html>
   <head>
      <title>BlockPage</title>
      <meta charset="utf-8">
      <link type="text/css" rel="stylesheet" href="css/table.css">
   </head>
   <body>
      ${body}
   </body>
   </html>`;
   return result;
}

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
   res.send('Hello World~!!');
});

app.get('/thanks', (req, res) => {
   res.send('Welcom 😊');
});

// login
app.post('/login', (req, res) => {
   const { id, pw } = req.body;
   const result = connection.query('select * from user where userid=? and passwd=?', [id, pw]);
   if (result.length == 0) {
      res.redirect('error.html');
   }
   if (id == 'admin' || id == 'root') {
      console.log(id + ' => Administrator Logined');
      res.redirect('member.html');
   } else {
      console.log(id + ' => User Logined');
      res.redirect('user.html');
   }
});

app.post('/register', (req, res) => {
   const { id, pw } = req.body;
   if (id == '') {
      res.redirect('register.html');
   } else {
      let result = connection.query('select * from user where userid=?', [id]);
      if (result.length > 0) {
         res.writeHead(200);
         let template = makeResultTemplate(`
         <div>
            <h3 style="margin-left: 30px">Registrer Failed</h3>
            <h4 style="margin-left: 30px">Already Exist ID.</h4>
            <a href="register.html" style="margin-left: 30px">Try Again</a>
         </div>`);
         res.end(template);
      } else {
         result = connection.query('insert into user values (?, ?)', [id, pw]);
         console.log(result);
         res.redirect('/');
      }
   }
});

app.get('/select', (req, res) => {
   const result = connection.query('select * from user;');
   console.log(result);
   res.writeHead(200);
   let temp = '';
   for (let i = 0; i < result.length; i++) {
      console.log(result[i].userid, result[i].passwd);
      temp += `<tr><td>${result[i].userid}</td><td>${result[i].passwd}</td></tr>`;
   }
   let resultPage = makeResultTemplate(` 
   <table border="1" style="margin: auto; text-align: center">
      <thead>
         <tr>
            <th>USER ID</th>
            <th>PASSWORD</th>
         </tr>
      </thead>
      <tbody>
         ${temp}
      </tbody>
   </table>`);
   res.end(resultPage);
});

app.get('/selectQuery', (req, res) => {
   const userid = req.query.userid;

   console.log(userid);
   const result = connection.query('select * from user where userid=?;', [userid]);
   res.writeHead(200);
   let resultPage = ``;
   if (userid == '') {
      resultPage = makeResultTemplate(`
         <div class="empty">
            Type Proper 'USERID'
         </div>
      `);
   } else if (result.length > 0) {
      let temp = '';
      for (let i = 0; i < result.length; i++) {
         console.log(result[i].userid, result[i].passwd);
         temp += `<tr><td>${result[i].userid}</td><td>${result[i].passwd}</td></tr>`;
      }
      resultPage = makeResultTemplate(` 
      <table border="1" style="margin: auto; text-align: center">
         <thead>
            <tr>
               <th>USER ID</th>
               <th>PASSWORD</th>
            </tr>
         </thead>
         <tbody>
            ${temp}
         </tbody>
      </table>
   `);
   } else {
      resultPage = makeResultTemplate(`
         <div class="empty">
            Any Data Doesn't Exist.
         </div> `);
   }
   res.end(resultPage);
});

app.post('/selectQuery', (req, res) => {
   const id = req.body.id;
   const result = connection.query('select * from user where userid=?', [id]);
   console.log(result);
   res.send(result);
});

app.post('/insert', (req, res) => {
   const { userid, pw } = req.body;
   const result = connection.query('insert into user values (?, ?)', [userid, pw]);
   console.log(result);
   res.redirect('/selectQuery?userid=' + req.body.userid);
});

app.post('/update', (req, res) => {
   const { userid, pw } = req.body;
   const result = connection.query('update user set passwd=? where userid=?', [pw, userid]);
   console.log(result);
   res.redirect('/selectQuery?userid=' + req.body.userid);
});

app.post('/delete', (req, res) => {
   const userid = req.body.userid;
   const result = connection.query('delete from user where userid=?', [userid]);
   console.log(result);
   res.redirect('/select');
});

module.exports = app;
