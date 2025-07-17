import socket
import threading
import os

def hidden_input(prompt=""):
    os.system("stty -echo")  # 關閉輸入回顯
    try:
        return input(prompt)
    finally:
        os.system("stty echo")  # 恢復輸入回顯

# 客戶端接收訊息
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except ConnectionResetError:
            print("伺服器關閉，結束連線")
            break

# 客戶端主程式
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('127.0.0.1', 12345))
        response = client_socket.recv(1024).decode()
        if "Unable to connect" in response:
            print(response)  # 顯示拒絕連線訊息
            client_socket.close()
            return
        else:
            print("Connected to the server.")
        
        if "Enter your name:" or "Name already in use. Please enter a different name:" in response:
            print("Enter your name:")
            username = input()
            client_socket.send(username.encode())
            response = client_socket.recv(1024).decode()
            print(response)

    except ConnectionRefusedError:
        print("無法連接到伺服器")
        return

    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start() 
    
    while True:
        message = hidden_input("") # 輸入不回顯
        if message.lower() == "exit":
            client_socket.send("exit".encode())
            print("You left the chat. Disconnected from server.")
            break
        client_socket.send(message.encode())

    client_socket.close()

if __name__ == "__main__":
    start_client()
