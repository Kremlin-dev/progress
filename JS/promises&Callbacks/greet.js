const greet = ()=>{
    return new Promise((resolve, reject)=>{
        setTimeout(()=>{
            resolve('Hello, welcome to JavaScript!');

        },2000)
    })
};

greet().then((msg)=>{
    console.log(msg)
}).catch((msg)=>{
    console.log(msg)
});