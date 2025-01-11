function signup() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch("/signup", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => alert(data.message));
}

function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            window.location.href = "/chatbot";
        } else {
            alert(data.message);
        }
    });
}

function sendMessage() {
    const message = document.getElementById("user-message").value;
    const chatBox = document.getElementById("chat-box");

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message })
    })
    .then(response => response.json())
    .then(data => {
        const botMessage = document.createElement("div");
        botMessage.textContent = "Bot: " + data.response;
        chatBox.appendChild(botMessage);
    });
}
