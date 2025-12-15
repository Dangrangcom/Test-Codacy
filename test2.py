var password = "123456";     // hard-coded secret

function login(user) {
    if (user == "admin") {  // == instead of ===
        console.log("login");
    }
}

eval("console.log('hack')"); // security issue

login("admin");
