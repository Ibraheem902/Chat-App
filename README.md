# Real-Time Chat App 💬

A fully functional, real-time chat application built with **Django**. This project leverages **WebSockets** and **Django Channels** to provide instant, seamless messaging between users. The front-end is beautifully structured and styled using custom **HTML** and **CSS**.

## ✨ Features

- ⚡ **Real-Time Messaging:** Instant communication powered by WebSockets and Django Channels (managed by the `a_rtchat` app).
- 👤 **User Management & Profiles:** Complete authentication system (login/signup) and user profile management, including custom avatars (`a_users` app).
- 📁 **File & Media Sharing:** Support for uploading and sharing files and images within chats.
- 🎨 **Clean & Responsive UI:** A user-friendly interface built from scratch with HTML5 and CSS3.

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Real-Time Infrastructure:** Django Channels, WebSockets (ASGI)
- **Frontend:** HTML5, CSS3
- **Package Management:** pip (Dependencies listed in `requirements.txt`)

## 📂 Project Structure

- `a_core/`: Main Django project settings, ASGI configuration, and core routing.
- `a_rtchat/`: Application handling real-time chat logic, WebSocket consumers, and message models.
- `a_users/`: Application responsible for user authentication, accounts, and profile data.
- `a_home/`: Base application for landing pages and general navigation.
- `templates/`: Centralized HTML templates used across the project.
- `static/`: Static assets including CSS stylesheets, JavaScript files, and static images.
- `media/`, `avatars/`, `files/`: Directories designated for user-uploaded content (profile pictures, shared chat files).

## 📄 License
This project is open-source and available under the MIT License.
