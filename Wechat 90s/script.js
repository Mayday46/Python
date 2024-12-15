
// Declare a variable to store the original height
let originalHeight = 300;

// Function to minimize the window
function minimizeWindow() {
    var loginContainer = document.querySelector('.login-container');

    // Store the original height if it's the first time minimizing
    if (!originalHeight) {
        originalHeight = loginContainer.offsetHeight;
    }

    loginContainer.style.height = '30px'; // Minimized height
    loginContainer.style.overflow = 'hidden'; // Hide content
}

// Function to maximize the window
function maximizeWindow() {
    var loginContainer = document.querySelector('.login-container');

    // Restore the original height if it was minimized
    if (originalHeight) {
        loginContainer.style.height = `${originalHeight}px`; // Restore original height
        loginContainer.style.overflow = 'visible'; // Show the content
    }
}

// Function to close the window
function closeWindow() {
    var loginContainer = document.querySelector('.login-container');
    loginContainer.style.display = 'none'; // Hide the entire login container
}

function signup() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    window.location.href = 'signup.html'
}

function login(){
    window.location.href = 'login.html'
}