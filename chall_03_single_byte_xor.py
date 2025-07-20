from set_01_utils import solve_single_byte_xor, hex_to_bytes

if __name__ == "__main__":
    enc = hex_to_bytes(
        '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
    print(solve_single_byte_xor(enc))
