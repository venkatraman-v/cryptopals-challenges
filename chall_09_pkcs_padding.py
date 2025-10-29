from set_02_utils import pkcs_pad
def test_pkcs_pad():
    assert pkcs_pad(b"YELLOW SUBMARINE", 20) == b"YELLOW SUBMARINE\x04\x04\x04\x04"
    print("pkcs_pad test passed")

if __name__ == '__main__':
    test_pkcs_pad()
