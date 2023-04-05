require('dotenv').config({ path: '.env' });

var axios = require('axios');
var data = JSON.stringify({
   collection: 'testdb',
   database: 'test',
   dataSource: 'Cluster0',
   projection: {
      id: 1,
      name: 1,
   },
});

var config = {
   method: 'post',
   url: 'https://us-west-2.aws.data.mongodb-api.com/app/data-dakbe/endpoint/data/v1/action/find',
   headers: {
      'Content-Type': 'application/json',
      'Access-Control-Request-Headers': '*',
      'api-key': process.env.ATLAS_API_KEY,
   },
   data: data,
};

axios(config)
   .then(function (response) {
      console.log(JSON.stringify(response.data));
   })
   .catch(function (error) {
      console.log(error);
   });
