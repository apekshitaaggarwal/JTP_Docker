import socket
from datetime import datetime
import threading

HOST = '0.0.0.0'
PORT = 5000

def log_message(message):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{now} - {message}")

def handle_client(conn, addr):
    log_message(f'Connected by {addr}')
    while True:
        data = conn.recv(1024)
        if not data:
            break
        log_message(f"Received: {data.decode()}")
        response = b'hello'
        log_message(f"Sending: {response.decode()}")
        conn.sendall(response)
    conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        log_message(f"Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

if __name__ == "__main__":
    main()
