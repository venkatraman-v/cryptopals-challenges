from set_01_utils import solve_single_byte_xor, base64_to_bytes, break_vigenere





if __name__ == "__main__":
    # read input and base64 decode
    try:
        base64_message = ""
        with open('chall_06_input.txt') as file:
            for line in file:
                base64_message += line.strip()
        message = base64_to_bytes(base64_message)
        # key_size, _ = find_best_key_size(message, 40)
        solution = break_vigenere(message, 40)
        print(str(solution).replace("\\n", "\n"))

    except FileNotFoundError:
        print("could not find file")
    # call break vigenere
    pass
