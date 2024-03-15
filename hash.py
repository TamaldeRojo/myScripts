import hashlib

def setUp(message,salt):
    hash = hashlib.pbkdf2_hmac('sha256',message,salt,444)
    hashed_message = hash.hex()
    print(hashed_message)
    return

if __name__ == "__main__":
    
    message = b"hola dios"
    salt = b"ahdjasdjajsdajskd"
    setUp(message,salt)
    
    pass