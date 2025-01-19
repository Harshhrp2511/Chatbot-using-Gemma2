document.getElementById("send-btn").addEventListener("click", function() {
    const userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") return;

    // Display the user's message
    const userMessage = document.createElement("div");
    userMessage.classList.add("user-message");
    userMessage.textContent = userInput;
    document.getElementById("chat-output").appendChild(userMessage);

    // Clear the input field
    document.getElementById("user-input").value = "";

    // You can replace the following with a call to Gemma2 for chatbot response
    const botMessage = document.createElement("div");
    botMessage.classList.add("bot-message");
    botMessage.textContent = "Bot: This is a placeholder response.";
    document.getElementById("chat-output").appendChild(botMessage);
});
