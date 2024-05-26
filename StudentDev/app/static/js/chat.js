// static/js/chat.js
var gname;

$(document).ready(function() {
    // Function to handle group click
    $('.group-list ul li').click(function() {
        var groupname = $(this).data('group');
        gname = groupname;
        // Send AJAX request to get chat messages
        $.ajax({
            url: '/get_chat_messages/' + groupname + '/',
            method: 'GET',
            success: function(data) {
                // Update the chat container with the fetched messages
                var chatContainer = $('.chat-container');
                chatContainer.empty(); // Clear existing messages
                var group_name = document.getElementById('Group-chat');
                group_name.innerText = 'Group Chat (' + gname + ')';
                
                data.forEach(function(message) {
                    var messageDiv = '<div class="message">' +
                                     '<span class="username">' + message.username + ':</span>' +
                                     '<span class="text">' + message.text + '</span>' +
                                     '</div>';
                    chatContainer.append(messageDiv);
                });
            }
        });
    });
});

// Function to send message to server
function sendMessage() {
    // Get the CSRF token from the cookie
    var csrftoken = getCookie('csrftoken');

    // Get the message from the input field
    var message = $('#textmessage').val();
    
    // Check if the message is not empty
    if (message.trim() !== '') {
        // Send AJAX request to the server to save the message
        $.ajax({
            url: '/send_message/',
            method: 'POST',
            headers: { "X-CSRFToken": csrftoken }, // Include CSRF token in the headers
            data: {
                'message': message,
                'groupname': gname
            },
            success: function(response) {
                // Display the sent message in the chat container
                var messageDiv = '<div class="message">' +
                                 '<span class="username">' + response.username + ':</span>' +
                                 '<span class="text">' + response.text + '</span>' +
                                 '</div>';
                $('.chat-container').append(messageDiv);
                // Clear the input field after sending the message
                $('#textmessage').val('');
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }
}

// Function to get CSRF token from cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Check if the cookie contains the CSRF token
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

