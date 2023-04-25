const https = require('https');

const data = JSON.stringify({
   todo: 'Read the book',
});

//post 일땐 header 필수
const optinos = {
   hostname: '192.168.1.12',
   port: 8000,
   path: '/todos',
   method: 'GET',
   header: {
      'Content-Type': 'application/json',
      'Content-Length': data.length,
   },
};

const req = https.request(optinos, res => {
   console.log(`statusCode : ${res.statusCode}`);
   res.on('data', d => {
      process.stdout.write(d);
   });
});

req.on('error', error => {
   console.log(error);
});

req.write(data);
req.end();
