function toggleChatbotPopup() {
    var popup = document.getElementById("chatbotPopup");
    var icon = document.getElementById("chatbotIcon");

    if (popup.style.display === "block") {
        popup.style.display = "none";
    } else {
        popup.style.display = "block";
    }
}

// function sendMessage() {
//     var chatInput = document.getElementById("chatInput");
//     var chatMessages = document.getElementById("chatMessages");

//     if (chatInput.value.trim() !== "") {
//         var userMessage = document.createElement("div");
//         userMessage.classList.add("user-message");
//         userMessage.textContent = chatInput.value;
//         chatMessages.appendChild(userMessage);

//         var botReply = document.createElement("div");
//         botReply.classList.add("bot-reply");
//         botReply.textContent = "This is bot reply";
//         chatMessages.appendChild(botReply);

//         chatInput.value = "";
//         chatMessages.scrollTop = chatMessages.scrollHeight; // Scroll to the bottom
//     }
// }

function sendMessage() {
    var chatInput = document.getElementById("chatInput");
    var chatMessages = document.getElementById("chatMessages");

    if (chatInput.value.trim() !== "") {
        var userMessage = chatInput.value;

        // Make an AJAX request to the Django backend
        $.post("/send_message/", { message: userMessage }, function(response) {
            // Create a new div for the user's message
            var userMessageDiv = document.createElement("div");
            userMessageDiv.classList.add("user-message");
            userMessageDiv.textContent = userMessage;
            chatMessages.appendChild(userMessageDiv);

            // Create a new div for the bot's reply
            var botReplyDiv = document.createElement("div");
            botReplyDiv.classList.add("bot-reply");
            botReplyDiv.textContent = response.bot_reply; 
            console.log(response.message)// Use the response from the server
            chatMessages.appendChild(botReplyDiv);

            // Clear the input field
            chatInput.value = "";

            // Scroll to the bottom of the chat messages
            chatMessages.scrollTop = chatMessages.scrollHeight;
        });
    }
}
