from set_01_utils import base64_to_bytes, ecb_encrypt, ecb_decrypt, xor, base64file_to_bytes, cbc_decrypt
# CBC is a mode
# each ciphtertext block is added to the next palintext block??


if __name__ == "__main__":
    ciphertext = base64file_to_bytes("chall_10_input.txt")
    print(str(cbc_decrypt(ciphertext, b"YELLOW SUBMARINE", b"\x00" * 16)).replace("\\n", "\n"))    
