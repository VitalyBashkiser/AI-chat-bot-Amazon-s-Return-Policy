# 🤖 AI Chatbot for Amazon's Return Policy
Welcome to the AI Chatbot project! This chatbot is designed to assist users with queries related to Amazon's Return Policy.
It's powered by OpenAI and trained using the data from Amazon's official return policy page.

# 🚀 Features
- Initial Greeting: The chatbot starts with a friendly greeting and an explanation of its functionality.
- Return Policy Queries: It provides accurate responses to questions about returning items, based on Amazon's return policy.
- Redirection for Unrelated Queries: If users ask questions not related to returns, the chatbot will politely guide them to contact Amazon customer support.
# 🛠️ Project Structure
The project consists of:

Telegram Bot: A bot that users can interact with directly on Telegram to get instant responses.
Web Script: A simple web interface that users can access via GitHub Pages.
# 📝 How to Use
## Telegram Bot
**Start the Bot: Click the link below to start chatting with the Telegram bot.**

**Start Chatbot on Telegram**
1. Ask a Question: Type your question related to Amazon's return policy.

2. Get Answers: Receive instant responses tailored to your query.

## Web Script (Demo)
[Visit the Web Page: Open the GitHub Pages link to access the chatbot's web interface](https://vitalybashkiser.github.io/AI-chat-bot-Amazon-s-Return-Policy/)

**Chatbot Web Interface**
1. Type Your Question: Enter your query in the chat window.

2. Receive Instant Replies: The chatbot will provide answers based on Amazon's return policy.

# 📝 Installation Guide
To integrate the chatbot into your website, add the following script just before the closing </body> tag on each page where you'd like the widget to appear:

```bash
    <script type="text/javascript">
      (function(d, t) {
          var v = d.createElement(t), s = d.getElementsByTagName(t)[0];
          v.onload = function() {
            window.voiceflow.chat.load({
              verify: { projectID: '66b78785cf5adb4c27b42242' },
              url: 'https://general-runtime.voiceflow.com',
              versionID: 'production'
            });
          }
          v.src = "https://cdn.voiceflow.com/widget/bundle.mjs"; v.type = "text/javascript"; s.parentNode.insertBefore(v, s);
      })(document, 'script');
    </script>
```
* Local Setup
To run this project on your local machine, follow these steps:

* Clone the repository:

```bash
git clone https://github.com/VitalyBashkiser/AI-chat-bot-Amazon-s-Return-Policy.git
```
* Launch the Chatbot:
Open the index.html file in your preferred web browser to start interacting with the chatbot.

# 📚 Technologies Used
- Python: Core programming language for the bot.
- Telegram API: Integration for the chatbot on Telegram.
- OpenAI: Language model powering the chatbot's responses.
- JavaScript: For the web-based chatbot interface.
- GitHub Pages: Hosting the web script for easy access.
# 🎯 Objective
This project was created as a test task to demonstrate the ability to build a functional AI chatbot within a short timeframe.
The goal was to create a user-friendly and effective solution that can handle specific queries related to Amazon's Return Policy.