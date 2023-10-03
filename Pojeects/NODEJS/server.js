// Creating an http server using nodeJS
const http = require('http');
const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res)=>{
    res.setHeader('Content-Type', 'text/plain');
    res.send('Hello Kremlin');
})
server.listen(hostname, port, ()=>{
    console.log('Server is listening on http://' + hostname + ':' + port + '/');


});