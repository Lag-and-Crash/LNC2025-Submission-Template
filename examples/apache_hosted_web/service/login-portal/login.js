const login = () => {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    if (username === "admin" && password === "password123") {
        const token = btoa("admin:password123");
        document.cookie = "token=" + token;
        window.location.href = "admin.html";
    } else {
        alert("Invalid username or password");
    }
}
