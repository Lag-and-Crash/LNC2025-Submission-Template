const checkAuth = () => {
    const cookies = document.cookie.split("; ");
    for (let i = 0; i < cookies.length; i++) {
        const parts = cookies[i].split("=");
        const name = parts[0];
        const value = parts[1];
        if (name === "token") {
            const token = atob(value);
            if (token === "admin:password123") {
                return true;
            } else {
                break;
            }
        }
    }
    window.location.href = "index.html";
}

if (!checkAuth()) {
    alert("Nice try.");
}