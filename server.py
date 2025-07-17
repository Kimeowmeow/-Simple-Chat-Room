import socket
import threading

# 伺服器設定
HOST = '127.0.0.1'
PORT = 12345
MAX_CLIENTS = 5

# 追蹤用戶
clients = {}
lock = threading.Lock() 

# 廣播訊息
def broadcast(message, sender_socket=None):
    with lock:
        for client_socket in clients:
            client_socket.send(message)

# 處理客戶端連線
def handle_client(client_socket, client_address):
    try:
        client_socket.send("Enter your name:".encode("utf-8"))
        username = client_socket.recv(1024).decode("utf-8")
        with lock:
            while username in clients.values():
                client_socket.send("Name already in use. Please enter a different name:".encode())
                username = client_socket.recv(1024).decode()
            clients[client_socket] = username
        broadcast(f"{username} has joined the chat.\n".encode())
        print(f"{username} has joined the chat")

        while True:
            message = client_socket.recv(1024).decode()
            if message.lower() == "exit":
                with lock:
                    del clients[client_socket]
                broadcast(f"{username} has left the chat.\n".encode())
                print(f"{username} has left the chat.")
                break
            formatted_message = f"{username}: {message}\n".encode()
            broadcast(formatted_message, client_socket)
    except ConnectionResetError:
        pass
    finally:
        client_socket.close()

# 啟動伺服器
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 使用TCP連線
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 允許重複使用address
    server_socket.bind((HOST, PORT)) 
    server_socket.listen(MAX_CLIENTS) 
    print(f"Server started on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept() # 接受客戶端連線
        
        with lock:
            if len(clients) >= MAX_CLIENTS: # 檢查是否達到最大連線數
                print(f"Connection attempt from {client_address} rejected: Maximum connections reached.")
                client_socket.send("Unable to connect to server: Maximum connections reached.".encode())
                client_socket.close()
            else:
                print(f"New connection from {client_address}")
                thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
                thread.start()

if __name__ == "__main__":
    start_server()
