const https = require('https');

const optinos = {
   hostname: '192.168.1.12',
   port: 8000,
   path: '/todos',
   method: 'GET',
};

const data = JSON.stringify({
   todo: 'Read the book',
});

const req = https.request(optinos, res => {
   console.log(`statusCode : ${res.statusCode}`);
   res.on('data', data => {
      process.stdout.write(data);
   });
});

req.on('error', error => {
   console.log(error);
});

req.write(data);
req.end();
