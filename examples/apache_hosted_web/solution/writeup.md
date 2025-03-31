# Solution
1. Visit the website, you are greeted with a login page.
2. View page source and locate the script tag, and read the source of `login.js`.
```js
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
```
3. The username and password is `admin` and `password123` respectively, as given by the source code.
4. Login with the credentials, and you will be redirected to `admin.html`.