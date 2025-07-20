from set_01_utils import unicode_to_bytes, bytes_to_hex, xor
if __name__=="__main__":
    input1 = unicode_to_bytes("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal")
    key = unicode_to_bytes("ICE")
    print(bytes_to_hex(xor(input1, key)))
    print()
    print((xor(xor(input1, key), key)))

    # print(bytes_to_hex(xor(input2, key)))
    