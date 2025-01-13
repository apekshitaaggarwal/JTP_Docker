import socket
import time
from datetime import datetime

servers = [('server1', 5000), ('server2', 5000)]
#servers = [('server-service', 5000)]
def log_message(server, message, sent_message):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{now} - Sent to {server}: {sent_message}")
    print(f"{now} - Received from {server}: {message}")

def send_hi(server):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(server)
            sent_message = 'hi'
            s.sendall(sent_message.encode())
            data = s.recv(1024)
            log_message(server, data.decode(), sent_message)
    except ConnectionRefusedError:
        log_message(server, "Server down. Retrying next...","down")
    except Exception as e:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"{now} - Error with {server}: {e}")

def main():
    while True:
        for server in servers:
            send_hi(server)
            time.sleep(1)

if __name__ == "__main__":
    main()
