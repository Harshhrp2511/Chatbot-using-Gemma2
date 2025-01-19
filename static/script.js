document.getElementById('chatForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const message = document.getElementById('message').value;
    const chatbox = document.getElementById('chatbox');
    const userMessage = document.createElement('div');
    userMessage.classList.add('user-message');
    userMessage.textContent = message;
    chatbox.appendChild(userMessage);
    
    // Send message to Flask server and get response
    fetch('/ask', {
        method: 'POST',
        body: new URLSearchParams({ message: message })
    })
    .then(response => response.text())
    .then(data => {
        const botMessage = document.createElement('div');
        botMessage.classList.add('bot-message');
        botMessage.textContent = data;
        chatbox.appendChild(botMessage);
    });

    document.getElementById('message').value = '';
});
