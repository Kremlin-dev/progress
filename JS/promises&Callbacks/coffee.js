//simulating a coffee making using promises

const makecoffee = new Promise((resolve, reject)=>{
console.log("Starting coffee-making process >>>");

setTimeout( ()=>{
    const coffee = Math.random();
    console.log(coffee);

    if (coffee > 0.5){
        resolve('Coffee has been made');
    }else{
        reject('Failed to make coffee')
    };
}, 3000)
});

makecoffee.then((mes)=>{
    console.log(mes)
}).catch((mes)=>{
    console.log(mes)
})