/*
 * Simple Javascript functions used by the course. Quick and dirty...
 * The storage functions are just meant to simplify some testing. So no usernames or passwords are used except locally in the pages  
 */

function hideDiv(id) {
    document.getElementById(id).classList.add("invisible");
}

function showDiv(id) {
    document.getElementById(id).classList.remove("invisible");
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
    // Get the current page, because we check loggedin on every page
    path = window.location.pathname;
    let currentPage = path.substring(path.lastIndexOf("/") + 1);

    // Logged in
    if(readStorageLoginUserName() == "letmein@gmail.com" && readStorageLoginPassword() == "secretpassword") {
        document.getElementById("showLogin").style.display = "none";
        document.getElementById("userLoggedIn").style.display = "block";
        document.getElementById("userName").innerHTML = readStorageLoginUserName();

        // Only set text if were on the signin page
        if(currentPage == "signin.html") {
            document.getElementById("checklogin-text").innerHTML =  "Logged in!";  
            document.getElementById("redirect-text").innerHTML = "Will redirect you to main page in 5 seconds...";  
            setTimeout(redirectURL, 5000);
        }     
         // Only set text if were on the index page. Members area visible
        if(currentPage == "index.html") {
            document.getElementsByClassName("members-area")[0].style.display = "block";
        }     
        
    }
    // Not logged in
    else {
        document.getElementById("showLogin").style.display = "block";
        document.getElementById("userLoggedIn").style.display = "none";

        // Only set text if were on the signin page
        if(currentPage == "signin.html") {
            document.getElementById("checklogin-text").innerHTML = "Wrong credentials!"; 
            document.getElementById("redirect-text").innerHTML = "Please try again...";
        }

        // Only set text if were on the index page. Members area not visible
        if(currentPage == "index.html") {
            document.getElementsByClassName("members-area")[0].style.display = "none";
        }     
    }
}

function redirectURL() {
    // Check if local development or published to GitHub.io. Different paths 
    let protocol = window.location.protocol + "//";
    let path = (window.location.host == "conrec-infinity-ab.github.io" ? "/Selenium-Course/index.html" : "/docs/index.html");
    let redirectURL  = protocol + window.location.host + path;
    document.location.href = redirectURL;
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