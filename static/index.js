console.log("%cIndex.js active", "color:red;font-size:24px")

let submitButton = document.getElementById("submitBtn");
let submitForm = document.getElementById("myForm");



submitButton.addEventListener("click", function (e) {
    e.preventDefault();
    console.log("Submitting...");

    const API = "http://127.0.0.1:5000/"

    let nameField = document.getElementById("name");
    let ageField = document.getElementById("age");
    let emailField = document.getElementById("email");
    let heightField = document.getElementById("height");
    let weightField = document.getElementById("weight");
    let genderField = document.getElementById("gender");
    let passwordField = document.getElementById("password");

    // Exact parameter names that server recives
    let primaryValues = {
        name: nameField.value,
        age: ageField.value,
        email: emailField.value,
        height: heightField.value,
        weight: weightField.value,
        gender: genderField.value,
        password: passwordField.value
    }

    console.log(primaryValues)

    let formData = new FormData()
    for (let key in primaryValues)
        formData.append(key, primaryValues[key])

    let params = {
        method: "POST",
        body: formData
    }

    fetch(API, params).then(response => response.text()).then((data) => {
        console.log(data);
        location.replace("/roadmap.html")
    })


})