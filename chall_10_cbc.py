from set_01_utils import base64_to_bytes
# CBC is a mode
# each ciphtertext block is added to the next palintext block??

def base64file_to_bytes(filename: str) -> bytes:
    string_base64 = ""
    with open(filename) as file:
        for line in file:
            string_base64 += line.strip()
    return base64_to_bytes(string_base64)

if __name__ == "__main__":
    ciphertext_base64 = ""
    with open("chall_08_input.txt") as file:
        for line in file:
            ciphertext_base64 += line.strip()

def make_blocks(message: bytes, block_size = 8) -> "list[bytes]":
    return [message[i: i + block_size] for i in range(0, len(message), block_size)]
# def cbc_encrypt(message:bytes, key:bytes):
    