//Js function is defined with the function keyword

function myname (name)
{

    // console.log(name)
    return name;

};

const value = myname("Isaac");

console.log(value)


//Anonymous functions have no function name but can be assigned to variables

const greet = function(){
    console.log("Hello World!")
};

greet()

//We also have arrow functions which are the newwe type of functions

const add = (a , b) => a + b;

console.log(add(2, 6))