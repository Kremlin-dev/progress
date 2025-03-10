const fetchdata = async ()=>{
    try{
        const response = await fetch('https://jsonplaceholder.typicode.com/posts/');

    const data = await response.json()

    console.log(data)

    if (data){
        console.log('Success')
    }else{
        console.log("Data could not be fetched")
    }
    } catch(error){
        console.log(error)
    }

};

fetchdata();