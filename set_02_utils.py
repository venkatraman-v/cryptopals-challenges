from set_01_utils import *
# -------------------CHALL 09--------------------------
def pkcs_pad(message: bytes, block_size: int) -> bytes:
    num_to_append = (block_size - (len(message) % block_size)) % block_size
    return message + bytes([num_to_append for _ in range(num_to_append)])

# -------------------CHALL 10--------------------------
def base64file_to_bytes(filename: str) -> bytes:
    string_base64 = ""
    with open(filename) as file:
        for line in file:
            string_base64 += line.strip()
    return base64_to_bytes(string_base64)

def make_blocks(message: bytes, block_size) -> "list[bytes]":
    return [message[i: i + block_size] for i in range(0, len(message), block_size)]

def cbc_encrypt(message:bytes, key:bytes, iv: bytes) -> bytes:
    assert len(key) == len(iv)
    assert len(key) == 16
    plaintext_blocks = make_blocks(message, 16)
    ciphertext = bytearray()
    prev_ciphertext_block = iv
    for plain_block in plaintext_blocks:
        ecb_input = xor(prev_ciphertext_block, plain_block)
        prev_ciphertext_block = ecb_encrypt(ecb_input, key)
        ciphertext += prev_ciphertext_block
    return bytes(ciphertext)

def cbc_decrypt(ciphertext:bytes, key:bytes, iv: bytes) -> bytes:
    assert len(key) == len(iv)
    assert len(key) == 16
    ciphertext_blocks = make_blocks(ciphertext, 16)
    plaintext = bytearray()
    prev_cipher_block = iv
    for cipher_block in ciphertext_blocks:
        ecb_input = ecb_decrypt(cipher_block, key)
        plaintext += xor(ecb_input, prev_cipher_block)
        prev_cipher_block = cipher_block
        
    return bytes(plaintext)
