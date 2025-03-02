// function to roll a dice 
// practice on promises

const dice = new Promise((resolve, reject)=>{
    const number = Math.floor(Math.random() * 6) + 1;
    console.log("Number rolled is:", number);

    if(number === 6){
        resolve('Congrats, You rolled a six (6)')
    } else{
        reject("sorry!, Try again.")
    };
});

dice.then((msg)=>{
    console.log(msg);
}).catch((msg)=>{console.log(msg)});