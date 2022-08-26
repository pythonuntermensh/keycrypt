from secrets import token_bytes
from typing import Tuple

def random_key(lenght: int):
    tb = token_bytes(lenght)
    return int.from_bytes(tb, 'big')

def encrypt(original_bytes: bytes) -> Tuple[int, int]:
    mazafaka = random_key(len(original_bytes))
    original_key = int.from_bytes(original_bytes, 'big')
    encrypted = original_key ^ mazafaka
    return mazafaka, encrypted

def decrypt(mazafaka: int, encrypted: int) -> bytes:
    decrypted = encrypted ^ mazafaka
    original_bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, 'big')
    return original_bytes


if __name__ == "__main__":
    picture: str = "U999_2_881x513.jpeg"
    with open(picture, 'rb') as f:
        original = f.read()
        key1, key2 = encrypt(original)
        with open('result.txt', 'w') as f:
            f.write(str(key1) + '\n' + str(key2))


    with open('result.txt', 'r') as f:
        key1 = int(f.readline())
        key2 = int(f.readline())
        decrypted = decrypt(key1, key2)
        with open('result.png', 'wb') as f:
            f.write(decrypted)

    
