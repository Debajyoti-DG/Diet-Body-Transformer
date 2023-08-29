// //TO CREATE A SERVER FOR GYMSITE AND RUN IT

// //Always mention the folder name first ... eg ... node .\JS\Server.js otheriwse we end up with module not found

// const http = require("http");
// const fs = require("fs");

// const local_host = '127.0.0.1';
// const port = 3000;


// const index = fs.readFileSync("./index.html");
// const roadmap = fs.readFileSync("./roadmap.html");
// // const css = fs.readFileSync("./style.css");
// // const fitness = fs.readFileSync("./Fitness.html");
// // const contact = fs.readFileSync("./Contact.html");

// const server = http.createServer((req, res) => {
//     console.log(req.url);

//     url=req.url;

//     res.statusCode = 200;
//     res.setHeader('Content-Type', 'text/html');
//     // res.end(home);

//     if (url == '/'){
//         res.end(index);
//     }

//     else if (url == '/roadmap'){
//         res.end(roadmap);
//     }
//     // else if (url == '/fitness'){
//     //     res.end(fitness);
//     // }
//     // else if (url == '/contact'){
//     //     res.end(contact);
//     // }
//     else{
//         res.statusCode=404;
//         res.end("<h1> Error 404 not found. </h1>");
//         // res.end(home);
//     }
// });

// server.listen(port, local_host, () => {
//     console.log(`Server is runnning at : http://${local_host}:${port}/`);
// });

// // console.log("kfhsiffdruighdiguhrfiogdkjgsedrifjofihdrfejgjkdrfslknkf");


// function ajaxpost () {


//     // // (A) GET FORM DATA
//     // var data = new FormData(document.getElementById("myForm"));

//     // // (B) AJAX REQUEST
//     // // (B1) POST DATA TO SERVER, RETURN RESPONSE AS TEXT
//     // fetch("1c-server.html", { method:"POST", body:data })
//     // .then(res => res.text())

//     // // (B2) SHOW MESSAGE ON SERVER RESPONSE
//     // .then(response => {
//     //   console.log(response);
//     //   if (response == "OK") { 
//     //     alert("SUCCESSFUL!"); 
//     // }
//     //   else { 
//     //     alert("FAILURE!"); 
//     // }
//     // })

//     // // (B3) OPTIONAL - HANDLE FETCH ERROR
//     // .catch(err => console.error(err));

//     // // (C) PREVENT FORM SUBMIT
//     // return false;


//     var data = new FormData();
//     data.append("name", document.getElementById("name").value);
//     data.append("email", document.getElementById("email").value);
//     data.append("age", document.getElementById("age").value);
//     data.append("height", document.getElementById("height").value);
//     data.append("weight", document.getElementById("weight").value);


//     var http = new XMLHttpRequest();
//     http.open("POST", "dummy.php");
//     http.onload = function(){
//         // alert(this.response);
//         alert("Success");
//     }
//     http.send(data);

//     return false;

// }


// function display(){

// }


function show_hide() {
    var x = document.getElementById('row-2');
    // let y = document.getElementById('item')
    if (x.style.display == 'none') {
        x.style.display = 'flex';
        x.style.justifyContent = 'center';
        x.style.alignItems = 'center';

        // After opening the bottom section
        // console.log(window.outerHeight)
        window.scrollTo(0, window.outerHeight)
    } else {
        x.style.display = 'none';
    }
}

document.querySelector("#show-login").addEventListener("click", function () {
    console.log("Clicked...")
    document.querySelector(".popup").classList.add("active");
});

document.querySelector(".popup .close-btn").addEventListener("click", function () {
    document.querySelector(".popup").classList.remove("active");
});

document.getElementById("redirectButton").addEventListener("click", () => {
    // if ()
    window.location = "/roadmap";
});
