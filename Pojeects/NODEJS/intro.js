// Accessing arguments from the command line in nodejs
//using process.argv to retrieve commandline arguments
const args = process.argv
const theargs=args.slice(2)

console.log(theargs)


//using process.env to access env variables
const username = process.env.USERNAME;
const nodeEnv = process.env.NODE_ENV;

console.log('Username:', username);
console.log('NODE_ENV:', nodeEnv);