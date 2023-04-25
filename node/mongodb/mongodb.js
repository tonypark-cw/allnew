const express = require('express');
const morgan = require('morgan');
const fs = require('fs');
const path = require('path');
const { MongoClient } = require('mongodb');
const mongoClient = require('mongodb').MongoClient;
const app = express();

app.set('port', process.env.PORT || 8000);
app.use(morgan('dev'));
const state = { db: null };
let dbURL = 'mongodb://192.168.1.15:27017';

app.get('/', (req, res) => {
   res.send('Welcome My Web Server');
});

app.get('/things', (req, res) => {
   mongoClient.connect(dbURL, { useUnifiedTopology: true }, function (err, client) {
      console.log('START');
      if (err != null) {
         res.json({ count: -1 });
      } else {
         state.db = client.db('test');
         state.db
            .collection('things')
            .find({})
            .toArray(function (err, result) {
               if (err) throw err;
               console.log('result : ');
               console.log(result);
               res.json(JSON.stringify(result));
            });
      }
   });
});

app.get('/seoul', (req, res) => {
   mongoClient.connect(dbURL, { useUnifiedTopology: true }, function (err, client) {
      console.log('START');
      if (err != null) {
         res.json({ count: -1 });
      } else {
         state.db = client.db('test');
         state.db
            .collection('seoul')
            .find({})
            .toArray(function (err, result) {
               if (err) throw err;
               console.log('result : ');
               console.log(result);
               res.json(JSON.stringify(result));
            });
      }
   });
});

app.get('/emp', (req, res) => {
   mongoClient.connect(dbURL, { useUnifiedTopology: true }, function (err, client) {
      console.log('START');
      if (err != null) {
         res.json({ count: -1 });
      } else {
         state.db = client.db('test');
         state.db
            .collection('emp')
            .find({})
            .toArray(function (err, result) {
               if (err) throw err;
               console.log('result : ');
               console.log(result);
               res.json(JSON.stringify(result));
            });
      }
   });
});

app.listen(app.get('port'), () => {
   console.log('8000 Port : Server Started ');
});
