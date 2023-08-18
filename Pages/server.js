//TO CREATE A SERVER FOR GYMSITE AND RUN IT

//Always mention the folder name first ... eg ... node .\JS\Server.js otheriwse we end up with module not found

const http = require("http");
const fs = require("fs");

const local_host = '127.0.0.1';
const port = 3000;


const index = fs.readFileSync("./index.html");
const roadmap = fs.readFileSync("./roadmap.html");
const css = fs.readFileSync("./style.css");
// const fitness = fs.readFileSync("./Fitness.html");
// const contact = fs.readFileSync("./Contact.html");

const server = http.createServer((req, res) => {
    console.log(req.url);

    url=req.url;

    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');
    // res.end(home);

    if (url == '/'){
        res.end(index);
    }

    else if (url == '/roadmap'){
        res.end(roadmap);
    }
    // else if (url == '/fitness'){
    //     res.end(fitness);
    // }
    // else if (url == '/contact'){
    //     res.end(contact);
    // }
    else{
        res.statusCode=404;
        res.end("<h1> Error 404 not found. </h1>");
        // res.end(home);
    }
});

server.listen(port, local_host, () => {
    console.log(`Server is runnning at : http://${local_host}:${port}/`);
});

// console.log("kfhsiffdruighdiguhrfiogdkjgsedrifjofihdrfejgjkdrfslknkf");