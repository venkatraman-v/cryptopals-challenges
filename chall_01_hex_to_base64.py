from set_01_utils import hex_to_bytes, bytes_to_base64


if __name__ == "__main__":
    enc_base64 = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print(hex_to_bytes(enc_base64))
    print(bytes_to_base64(hex_to_bytes(enc_base64)))