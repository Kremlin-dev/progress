//learning promises in javascript


// const failed = ()=>{
//     console.log("This promise failed")
// }

// const done = ()=>{
//     console.log("This promise was a success")
// }
//  const promise = new Promise((resolve, reject)=>{
//     setTimeout(()=>{
//         resolve() 
//     }, 2000)
   
//     })
// const ppromise = new Promise((resolve, reject)=>{
//     setTimeout(()=>{
//         reject()  


//     }, 2000)
    
// })

// promise.then(()=>{
//     console.log("Success");
// })
// ppromise.catch(()=>{
//     console.log("Failed");
// })

// creating a promise
const promise = new Promise((resolve, reject) => {
    setTimeout(()=>{
        resolve("Made it")
    }, 1000)
    
})

promise.then((result)=>{
    console.log(result)
    console.log("Here I am");
})