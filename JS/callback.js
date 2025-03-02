// Callback functions are functions passed as arguments to other functions


function calculator (a, b, Callback){

    const sum = a + b;
    Callback(sum);
}

const display = (result)=> {console.log("The result after callback is:", result)}


calculator(2, 5, display)

//Callback functions are used in asynchronous scenarios

