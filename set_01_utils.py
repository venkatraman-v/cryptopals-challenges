# Data conversion formats
from typing import Union
from Crypto.Cipher import AES
# -------------------CHALL 01--------------------------
def hex_digit_to_int(input: str) -> int:
    if input[0] in "1234567890":
        return ord(input[0]) - ord("0")
    elif input[0] in "abcdefghijklmnopqrstuvwxyz":
        return ord(input[0]) - ord("a") + 10 
    elif input[0] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return ord(input[0]) - ord("A") + 10
    else:
        raise Exception(f"unrecognized character {input[0]}")

def hex_to_bytes(input: str) -> bytes:
    ret = bytearray()
    for i in range(0, len(input), 2):
        ret.append(16 * hex_digit_to_int(input[i]) + hex_digit_to_int(input[i + 1]))
    return bytes(ret)

def num_to_base_64(num: int):
    if num < 26:
        return chr(num + ord("A"))
    elif num < 52:
        return chr(num - 26 + ord("a"))
    elif num < 62:
        return str(num - 52)
    elif num == 62:
        return "+"
    elif num == 63:
        return "/"
    else:
        raise Exception(f"unrecognized num {num}")

def bytes_to_base64(input: Union[bytearray, bytes]) -> str:
    base64_arr = []
    i = 0
    pad = 0 
    while i < len(input):
        # Get up to 3 bytes (24 bits)
        b = input[i:i+3]
        # Pad with zeros if less than 3 bytes
        pad = 3 - len(b)
        b += b'\x00' * pad
        # Combine into a single integer
        n = (b[0] << 16) + (b[1] << 8) + b[2]
        # Extract 4 base64 digits
        for j in range(18, -1, -6):
            base64_arr.append(num_to_base_64((n >> j) & 0x3F))
        i += 3
    # Adjust for padding
    if pad:
        base64_arr = base64_arr[:-pad] + ["="] * pad
    return "".join(base64_arr)

def int_to_hex(a_byte: int) -> str:
    assert a_byte >= 0, "cannot convert negative to hex"
    if a_byte < 10:
        return str(a_byte)
    if a_byte < 16:
        return chr(ord('a') + a_byte - 10)
    else:
        return int_to_hex(a_byte // 16) + int_to_hex(a_byte % 16)

def bytes_to_hex(input: bytes) -> str:
    return "".join([int_to_hex(a_byte) for a_byte in input])
    
# -------------------CHALL 02--------------------------
def fixed_xor(arg1: bytes, arg2: bytes) -> bytes:
    assert len(arg1) == len(arg2), "Trying to xor mismatched lengths!"
    return bytes([arg1[i] ^ arg2[i] for i in range(len(arg1))])

# -------------------CHALL 03--------------------------
def score(message: str) -> int:
    score = 0
    for character in message:
        if character in 'ETAOIN SHRDLUetaoinshrdlu':
            score += 1
    return score


def score2(message: str) -> float:
    letterFrequency = {'E': 12.0,
                       'T': 9.10,
                       'A': 8.12,
                       'O': 7.68,
                       'I': 7.31,
                       'N': 6.95,
                       'S': 6.28,
                       'R': 6.02,
                       'H': 5.92,
                       'D': 4.32,
                       'L': 3.98,
                       'U': 2.88,
                       'C': 2.71,
                       'M': 2.61,
                       'F': 2.30,
                       'Y': 2.11,
                       'W': 2.09,
                       'G': 2.03,
                       'P': 1.82,
                       'B': 1.49,
                       'V': 1.11,
                       'K': 0.69,
                       'X': 0.17,
                       'Q': 0.11,
                       'J': 0.10,
                       'Z': 0.07}
    score = 0
    for character in message:
        if character.upper() in letterFrequency:
            score += letterFrequency[character.upper()] + 50
    return score


def bytes_to_unicode(message: bytes) -> str:
    return "".join([chr(a_byte) for a_byte in message])

def solve_single_byte_xor(message: bytes) -> "tuple[bytes, bytes, float]":
    best = (b'key', b'message', -1)
    for i in range(256):
        key = bytes([i] * len(message))
        cand_message = fixed_xor(message, key)
        cand_score = score(bytes_to_unicode(cand_message))
        if best[2] < cand_score:
            best = (key[0:1], cand_message, cand_score)
    return best
# -------------------CHALL 04--------------------------


# -------------------CHALL 05--------------------------
def xor(message: bytes, key: bytes) -> bytes:
    assert len(message) >= len(key)
    ret = []
    for i in range(len(message)):
        ret.append(message[i] ^ key[i % len(key)])
    return bytes(ret)

def unicode_to_bytes(text: str) -> bytes:
    return bytes([ord(a_byte) for a_byte in text])


# -------------------CHALL 06--------------------------
def num_ones(an_int: int) -> int:
    ret = 0
    for dig in bin(an_int)[2:]:
        if dig == '1':
            ret += 1
    return ret

def hamming_distance(arg1: bytes, arg2: bytes) -> int:
    ret = 0
    assert len(arg1) == len(arg2), "Cannot find Hamming distance of different lengths"
    for i in range(len(arg1)):
        ret += num_ones(arg1[i] ^ arg2[i])
    return ret

def find_best_key_size(message: bytes, max_key_size: int) -> "tuple[int, float]":
    best_keysize = (-1, 8) # key size, average hamming distance
    for key_size in range(1, max_key_size + 1):
        blocks = [message[i: i + key_size] for i in range(0, len(message), key_size)]
        blocks.pop() # removes any potential for partial block
        hamming_distances = [hamming_distance(blocks[i], blocks[i + 1]) for i in range(len(blocks) - 1)]
        avg_hamming_distance = sum(hamming_distances) / len(hamming_distances) / key_size
        if best_keysize[1] > avg_hamming_distance:
            best_keysize = (key_size, avg_hamming_distance)
    return best_keysize
        
def base64_digit_to_int(a_base64_digit: str) -> int:
    if a_base64_digit in "QWERTYUIOPASDFGHJKLZXCVBNM":
        return ord(a_base64_digit) - ord('A')
    elif a_base64_digit in "qwertyuiopasdfghjklzxcvbnm":
        return ord(a_base64_digit) - ord('a') + 26
    elif a_base64_digit in "1234567890":
        return int(a_base64_digit) + 52
    elif a_base64_digit == '+':
        return 62
    elif a_base64_digit == '/':
        return 63
    else:
        raise Exception(f"Tried to base64 decode unrecognized digit {a_base64_digit.encode('unicode_escape').decode('latin-1')}")
    
def base64_to_bytes(message: str) -> bytes:
    ret = []
    num_eq = message.count('=')
    message = message.strip('= ')
    message_int = [base64_digit_to_int(a_base64_digit) for a_base64_digit in message]
    for i in range(3, len(message_int), 4):
        ret += [(message_int[i - 3] << 2) + (message_int[i - 2] >> 4), 
                ((message_int[i - 2] & 0xf) << 4) + (message_int[i - 1] >> 2),
                ((message_int[i - 1] & 0x3) << 6) + (message_int[i])]
    if num_eq == 1:
        ret += [(message_int[-3] << 2) + (message_int[-2] >> 4), 
                ((message_int[-2] & 0xf) << 4) + (message_int[-1] >> 2)]
    if num_eq == 2:
        ret += [(message_int[-2] << 2) + (message_int[-1] >> 4)]
    return bytes(ret)

def break_vigenere(message: bytes, max_key_size = 40) -> bytes:
    best_key_size, _ = find_best_key_size(message, max_key_size)
    transposed_blocks = [message[i::best_key_size] for i in range(best_key_size)]
    transposed_solution = [solve_single_byte_xor(message_block)[1] for message_block in transposed_blocks]
    solution = [transposed_solution[i % best_key_size][i // best_key_size] for i in range(len(message))]
    return bytes(solution)


# -------------------CHALL 07--------------------------
def ecb_decrypt(ciphertext: bytes, key: bytes) -> bytes:
    AES.MODE_ECB= 1
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)
def ecb_encrypt(ciphertext: bytes, key: bytes) -> bytes:
    AES.MODE_ECB= 1
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(ciphertext)

# -------------------CHALL 08--------------------------
# -------------------CHALL 09--------------------------
def pkcs_pad(message: bytes, block_size: int) -> bytes:
    num_to_append = block_size - len(message)
    if num_to_append < 0:
        raise Exception("Length of message is greater than pad length")
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

# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
# -------------------CHALL 03--------------------------
