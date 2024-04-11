/*
 * Simple Javascript functions used by the course. 
 * The stiorage functions are just meant to simplify some testing. So no usernames or passwords are used except locally in the pages  
 */

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

function submitLogin() {
    setStorageLogin();
    
    let redirectURL = "http://" + window.location.hostname + window.location.pathname + "/signin.html";
    window.location.replace(redirectURL);

    // Debug
    //alert(redirectURL);
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

// function tests() {
//     setStorageLogin();
//     alert("Text: " + readStorageLoginUserName());
//     alert("Text: " + readStorageLoginPassword());
// }