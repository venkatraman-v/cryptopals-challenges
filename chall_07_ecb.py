from set_01_utils import base64_to_bytes, ecb_decrypt
if  __name__ == "__main__":
    ciphertext_base64 = ""
    with open("set_01_basics/chall_07_input.txt") as file:
        for line in file:
            ciphertext_base64 += line.strip()
    ciphertext = base64_to_bytes(ciphertext_base64)
    plaintext = ecb_decrypt(ciphertext, b"YELLOW SUBMARINE")
    print(str(plaintext).replace("\\n", "\n"))