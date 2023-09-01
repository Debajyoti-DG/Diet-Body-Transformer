let c=0
let d=0

document.querySelector("#yes-btn").addEventListener("click", () =>{
    console.log("Yes clicked........");
    c=c+1
    d=d+1
    console.log(c);
    percentage = c/d*100;
    if (percentage <=40){
        str = "We understand it has been a tough journey so far. Try harder next time champ !"
    }
    else if (percentage <=80){
        str = "Well Done ! Your performance is quite decent. We highly appreciate it. Keep it up dude !"
    }
    else{
        str = "Excellent performance ! You have increased your limits and pushed yourself beyond your boundaries. Keep going !"
    }
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
        alert(str);
        window.location.href="/"
    }
})

document.querySelector("#no-btn").addEventListener("click", () =>{
    console.log("No clicked........");
    c=c+0
    d=d+1
    console.log(c);
    // console.log("Your perfomance rating is : " + c/d*100 + "%");
    percentage = c/d*100;
    if (percentage <=40){
        str = "We understand it has been a tough journey so far. Try harder next time champ !"
    }
    else if (percentage <=80){
        str = "Well Done ! Your performance is quite decent. We highly appreciate it. Keep it up dude !"
    }
    else{
        str = "Excellent performance ! You have increased your limits and pushed yourself beyond your boundaries. Keep going !"
    }
    if (d<=30){
        console.log("Your perfomance rating is : " + percentage + "%");
        document.getElementById("analytics").innerHTML = "Your performance Rating is : " + percentage + "%";
    }
    else{
        document.getElementById("analytics").innerHTML = "Your session is over";
        alert("Your Session is over");
        alert(str);
        window.location.href="/"
    }
})
