let c=0
let d=0

document.querySelector("#yes-btn").addEventListener("click", () =>{
    console.log("Yes clicked........");
    c=c+1
    d=d+1
    console.log(c);
    percentage = c/d*100;
    if(d<=30){
        console.log("Your perfomance rating is : " + percentage + "%");
        document.getElementById("analytics").innerHTML = "Your performance Rating is : " + percentage + "%";
    }
    else{
        document.getElementById("analytics").innerHTML = "Your session is over";
        alert("Your session is over");
        for(i=1;i<1000;i++){
            console.log();
        }
        window.location.href="/index.html"
    }
})

document.querySelector("#no-btn").addEventListener("click", () =>{
    console.log("No clicked........");
    c=c+0
    d=d+1
    console.log(c);
    // console.log("Your perfomance rating is : " + c/d*100 + "%");
    percentage = c/d*100;
    if (d<=30){
        console.log("Your perfomance rating is : " + percentage + "%");
        document.getElementById("analytics").innerHTML = "Your performance Rating is : " + percentage + "%";
    }
    else{
        document.getElementById("analytics").innerHTML = "Your session is over";
        alert("Your Session is over");
        window.location.href="/index.html"
    }
})
