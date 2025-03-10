//This is to demonstrate more on callback functions and async programming


const fetchdata = ()=> {
    console.log("fetching data now")
};

setTimeout( () =>{ console.log("Data has been fetched")}, 2000);

fetchdata()

