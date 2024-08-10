document.addEventListener("DOMContentLoaded", function() {
    const chatBox = document.createElement("div");
    chatBox.id = "chatBox";
    document.body.appendChild(chatBox);

    const inputField = document.createElement("input");
    inputField.type = "text";
    inputField.placeholder = "Type your message...";
    document.body.appendChild(inputField);

    const sendButton = document.createElement("button");
    sendButton.innerText = "Send";
    document.body.appendChild(sendButton);

    sendButton.addEventListener("click", function() {
        const userMessage = inputField.value;
        inputField.value = "";

        fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userMessage }),
        })
        .then(response => response.json())
        .then(data => {
            const reply = data.reply;
            const messageDiv = document.createElement("div");
            messageDiv.innerText = reply;
            chatBox.appendChild(messageDiv);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
