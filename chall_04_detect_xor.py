# from chall_03_single_byte_xor import solve_single_byte_xor, hex_to_bytes
from set_01_utils import solve_single_byte_xor, hex_to_bytes
if __name__=="__main__":
    try:
        best = (b'key', b'message', -5043)
        with open("chall_04_strings.txt", 'r') as file:
            for line in file:
                solved = solve_single_byte_xor(hex_to_bytes(line.strip()))
                if best[2] < solved[2]:
                    best = solved
        print(best)
    except FileNotFoundError:
        print("not found lolz")