const placeorder = (fooditem)=>{
    return new Promise( function(resolve, reject){
        console.log("New promise created");

        setTimeout(()=>{
            if (fooditem){
                resolve("passed");
            } else{reject('failed');}
            
        }, 200)
    });
};

placeorder("Banku").then(message=>console.log(message))
.catch(error=> console.log(error))

