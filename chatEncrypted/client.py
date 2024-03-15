import socket
from cryptography.fernet import Fernet
from icecream import ic


def main(socket) -> None:
    serverHost = '10.100.2.237'
    serverPort = 9090
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverHost,serverPort))
    
    try:
      clientSocket.send(input("Enter your phone number: ").encode('utf-8'))
      
      key = clientSocket.recv(2048).decode('utf-8')
      print(f"Diese ist die key: {key}")
      hashKey = Fernet(key)
      
      while True:
        
        msg = input("Enter a msg: ")
        if msg.lower() == 'quit':
            break
        
        msg = msg.encode('utf-8')
        msgEncrypted = hashKey.encrypt(msg)
        
        clientSocket.send(msgEncrypted)
        
        print(f"Server sagte: {clientSocket.recv(2048).decode('utf-8')}")
    except Exception as e:
      print(f'An exception occurred {e}')
    finally:
        clientSocket.close()
        
if __name__ == "__main__":
    main(socket)
    
