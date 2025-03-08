
const login = (username, password) =>{
    return new Promise((resolve, reject)=>{
        if(username ==='Kremlin' && password ==="admin"){
            resolve('Login successful')
        }
        else{
            reject('Incorrect username or Password')
        };
    })
};

login('Kremlin', 'admin').then((success)=>{
    console.log(success)
}).catch((error)=>{
    console.log(error)
});



const Login = async  (username, password)=>{

    try{
        const response = await fetch('https://kremhub.com');
    const data = await response.json();

    if(data.username === username && data.password === password){
        console.log(data)
    }else{
        console.log('error')
    }
    }catch(error){
        console.log("login failed")
    }

};

Login();