# 📡 Simple Chat Room – Next-Gen Wireless Networks HW3

## 📘 Project Overview

This project implements a simple chat room system using **TCP socket programming**. The goal is to simulate server-client communication and user interaction in a multi-user environment.

- Learn basic socket and multi-threading programming.
- Understand server-client broadcast and user registration.
- Implement name input, message transmission, disconnection handling, and more.

📌 This system could be the foundation for future social, communication, or e-learning chat applications.

## 🛠️ System Architecture

- **Server (`server.py`)**
  - Accepts up to 5 TCP connections from clients.
  - Handles username registration, broadcasting, and disconnection.
  - Uses `threading` to support concurrent connections.

- **Client (`client.py`)**
  - Connects to the server with a username.
  - Sends and receives broadcast messages.
  - Supports `exit` command to leave the chat.
  - Uses custom `hidden_input()` to hide message input on local terminal.

## 🚀 How to Run

1. **Start the Server**
   ```bash
   python3 server.py
   ```

2. **Start the Client**
   ```bash
   python3 client.py
   ```

## 📋 Features

- Multi-client connection with real-time message broadcasting.
- Username uniqueness enforcement.
- Exit and reconnect supported.
- No echo on local input; messages are only shown after server broadcast.
- Rejects connection after 5 clients, with appropriate message.

## 🧠 Technical Notes

- `threading.Lock()` used to protect shared `clients` data.
- `setsockopt(SO_REUSEADDR)` enables address reuse on restart.
- Terminal echo is turned off using `termios` + `tty`.

## 📁 File Structure

| File          | Description                     |
|---------------|----------------------------------|
| `server.py`   | Server-side code                 |
| `client.py`   | Client-side code                 |
| `README.md`| This documentation     |

## 📌 Notes

- Requires Python 3.
- Recommended to run on UNIX-based systems (Linux/macOS).
