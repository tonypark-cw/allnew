const express = require('express');
const https = require('https');
const request = require('request');
const CircularJSON = require('circular-json');

const app = express();

let option = 'http://192.168.1.78:8000/hello';

app.get('/', (req, res) => {
   res.send('ServerStarted');
});

app.get('/hello', (req, res) => {
   res.send('Hello World - Tony');
});

app.get('/rhello', (req, res) => {
   request(option, { json: true }, (err, result, body) => {
      if (err) return console.log(err);
      console.log(body);
      res.send(CircularJSON.stringify(body));
   });
   // https.request(option, res => {
   //    console.log(`statusCode : ${res.statusCode}`);
   //    res.on('data', d => {
   //       process.stdout.write(d);
   //    });
   // });
});

option = 'http://192.168.1.78:8000/data';

const data = JSON.stringify({ todo: 'Book a ticket - Tony' });
app.get('/data', (req, res) => {
   res.send(data);
});

app.get('/rdata', (req, res) => {
   request(option, { json: true }, (err, result, body) => {
      if (err) return console.log(err);
      console.log(body);
      res.send(CircularJSON.stringify(body));
   });
});

app.listen(8120, () => {
   console.log('8120 PORT : Server Started');
});

module.exports = app;
