from set_01_utils import hex_to_bytes, fixed_xor, bytes_to_hex

if __name__ == "__main__":
    arg1 = hex_to_bytes('1c0111001f010100061a024b53535009181c')
    arg2 = hex_to_bytes('686974207468652062756c6c277320657965')
    print(fixed_xor(arg1, arg2))
    print(bytes_to_hex(fixed_xor(arg1, arg2)))