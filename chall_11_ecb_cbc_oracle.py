from set_01_utils import ecb_encrypt, ecb_decrypt
from set_02_utils import cbc_encrypt, cbc_decrypt, pkcs_pad
import os
from typing import Callable, Literal

def black_box(message: bytes) -> "tuple[bytes,bytes,bytes]":
    message = pkcs_pad(message, 16)
    key = os.urandom(16)
    if os.urandom(1)[0] > 128:
        # Encrypt with CBC
        iv = os.urandom(16)
        return (cbc_encrypt(message, key, iv), key, iv)
    else:
        # Encrypt with ECB
        return (ecb_encrypt(message, key), key, b"")

def test_black_box():
    test_message = pkcs_pad(b"I know your friends say\n\"When you know, you know\"\nI just don't know right now", 16)
    black_box_output = black_box(test_message)
    while len(black_box_output[2]) != 0:
        black_box_output = black_box(test_message)
    assert ecb_decrypt(black_box_output[0], black_box_output[1]) == test_message
    while len(black_box_output[2]) == 0:
        black_box_output = black_box(test_message)
    assert cbc_decrypt(black_box_output[0], black_box_output[1], black_box_output[2]) == test_message
    print("Black box works")
    
    

def ecb_oracle(black_box: Callable[[bytes], bytes]) -> bool:
    uniform_bytes = b"qwoivjvx" * 4
    encrypted = black_box(uniform_bytes)
    return str(encrypted[:16]) == str(encrypted[16:])
    
def test_oracle():
    for i in range(100):
        if os.urandom(1)[0] > 128:
            # Encrypt with CBC
            # iv = os.urandom(16)
            # return (cbc_encrypt(message, key, iv), key, iv)
            assert not ecb_oracle(lambda x: cbc_encrypt(x, os.urandom(16), os.urandom(16)))
        else:
            # # Encrypt with ECB
            # return (ecb_encrypt(message, key), key, b"")
            assert ecb_oracle(lambda x: ecb_decrypt(x, os.urandom(16)))
    print("Oracle works")

if __name__ == "__main__":
    test_black_box()
    test_oracle()