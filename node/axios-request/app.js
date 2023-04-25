const axios = require('axios');
axios
   .post('http://192.168.1.15:8000/todos', {
      todo: 'Read the book',
   })
   .then(res => {
      console.log(`statusCode : ${res.status}`);
      console.log(res);
   })
   .catch(error => {
      console.log(error);
   });
