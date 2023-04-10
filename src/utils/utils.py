import hashlib 

def hash_string(string : str) -> str:
    hashed_string = hashlib.md5(string.encode())
    return hashed_string.hexdigest()