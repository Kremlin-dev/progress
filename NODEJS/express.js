// creating an HTTP server using express

// 1. import the express module
const express = require('express')

 //2. create an instance of the module to use
const app = express();
const port = 3000;

app.get('/home', (req, res)=>{
    res.end("Hello");
})

app.listen(port, ()=>{
    console.log("The server has started");
})


