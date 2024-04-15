/*
 * Simple Javascript functions used by the course. Quick and dirty...
 * The storage functions are just meant to simplify some testing. So no usernames or passwords are used except locally in the pages  
 */

function hideDiv(id) {
    document.getElementById(id).classList.add("invisible")
}

function showDiv(id) {
    document.getElementById(id).classList.remove("invisible")
}

function getNavbarUserName() {
    return document.getElementById("navbarEmail").value;
}

function getNavbarPassword() {
    return document.getElementById("navbarPassword").value;
}

function setStorageLogin() {
    sessionStorage.setItem("userName", getNavbarUserName());
    sessionStorage.setItem("password", getNavbarPassword());
}

function clearStorageLogin() {
    sessionStorage.clear();
}

function readStorageLoginUserName() {
    return sessionStorage.getItem("userName");
}

function readStorageLoginPassword() {
    return sessionStorage.getItem("password");
}

function validateLogin() {
    if(readStorageLoginUserName() == "letmein@gmail.com" && readStorageLoginPassword() == "secretpassword") {
        document.getElementById("showLogin").style.display = "none";
        document.getElementById("userLoggedIn").style.display = "block";
        document.getElementById("userName").innerHTML = readStorageLoginUserName();  
        document.getElementsByClassName("checklogin")[0].innerHTML =  "Logged in!"      
    }
    else {
        document.getElementById("showLogin").style.display = "block";
        document.getElementById("userLoggedIn").style.display = "none";
        document.getElementsByClassName("checklogin")[0].innerHTML = "Wrong credentials! Please try again."
    }
}

function confirmButton() {
    let userClick = confirm("An alert with Cancel & OK buttons");
    document.getElementById("confirm_text").innerHTML = "Output: " + (userClick ? "OK" : "Cancel"); 
  }

function promptButton() {
    let text;
    let name = prompt("Please enter your name:", "Peps Persson");
    if (name == null || name == "") {
      text = "Output: User cancelled";
    } else {
      text = "Output: " + name;
    }
    document.getElementById("prompt_text").innerHTML = text;
  }