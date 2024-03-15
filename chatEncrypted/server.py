import socket
from cryptography.fernet import Fernet
from icecream import ic

def setUp():
    port = 9090
    host = socket.gethostbyname(socket.gethostname())
    
    print(f"Zuhoren {host}") 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server.bind((host,port))
    server.listen(2)
    
    return server

def serverConn(server):
    connData, addr = server.accept()
    print(f"Verbunden mit dieser {addr}")
    try:
        num = connData.recv(2048).decode('utf-8')
        print(num)
        
        
        data = genKey()
        connData.send(data[0])
        while True:
            #Gen hash aqui?
            
            msg = connData.recv(2048).decode('utf-8')
            
            hashKey = data[1]
            decriptedMsg = hashKey.decrypt(msg)
            
            print(f"{num} sagte: {decriptedMsg}")
            
            response = input('Enter a response: ')
            if response.lower() == 'quit':
                break    
            connData.send(response.encode('utf-8'))
                                
    except Exception as e:
      print(f'Something went wrong: {e}')
    finally:
        connData.close()
    return

def genKey():
    key=Fernet.generate_key()
    print(f"Diese ist die: ", key.decode('utf-8'))
    hashHey = Fernet(key.decode('utf-8'))
    return [key,hashHey]

def main() -> None:
    server = setUp()
    serverConn(server)
    
    

if __name__ == "__main__":
    main()
    
