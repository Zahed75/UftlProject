let searchBar = document.getElementById("search");
let loginButton = document.getElementById("login-btn");
let signupButton = document.getElementById("signup-btn");

searchBar.addEventListener('mouseenter', () => {
    loginButton.style.display = "none";
    signupButton.style.display = "none";
});

searchBar.addEventListener('mouseleave', () => {
    setTimeout(() => {
        loginButton.style.display = "block";
        signupButton.style.display = "block";
    }, 200);
});
