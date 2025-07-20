from set_01_utils import *

def test_hex_digit_to_int():
    assert hex_digit_to_int("0") == 0, "'0' -> 0 failed"
    assert hex_digit_to_int("3") == 3, "'3' -> 3 failed"
    assert hex_digit_to_int("E") == 14, "'E' -> 15 failed"
    assert hex_digit_to_int("e") == 14, "'e' -> 15 failed"
    assert hex_digit_to_int("A") == 10, "'A' -> 10 failed"
    assert hex_digit_to_int("a") == 10, "'a' -> 10 failed"
    print("test_hex_digit_to_int passed")


def test_bytes_to_base64_basic():
    # Test with known input/output pairs
    assert bytes_to_base64(b"Man") == "TWFu", "Failed for 'Man'"
    assert bytes_to_base64(b"Ma") == "TWE=", "Failed for 'Ma'"
    assert bytes_to_base64(b"M") == "TQ==", "Failed for 'M'"
    assert bytes_to_base64(b"any carnal pleasure.") == "YW55IGNhcm5hbCBwbGVhc3VyZS4=", "Failed for 'any carnal pleasure.'"

def test_bytes_to_base64_empty():
    assert bytes_to_base64(b"") == "", "Failed for empty input"

def test_bytes_to_base64_hex_input():
    # Test with the input from the file
    hex_input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    expected_b64 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    assert bytes_to_base64(hex_to_bytes(hex_input)) == expected_b64, "Failed for hex input"

def test_bytes_to_base64_padding():
    # Test for correct padding
    assert bytes_to_base64(b"any carnal pleasure") == "YW55IGNhcm5hbCBwbGVhc3VyZQ==", "Failed for padding (2 =)"
    assert bytes_to_base64(b"any carnal pleasur") == "YW55IGNhcm5hbCBwbGVhc3Vy", "Failed for no padding"

def test_bytes_to_base64_non_ascii():
    # Test with non-ASCII bytes
    data = bytes([0xff, 0xee, 0xdd, 0xcc, 0xbb, 0xaa])
    assert bytes_to_base64(data) == "/+7dzLuq", "Failed for non-ASCII bytes"



if __name__ == "__main__":
    test_bytes_to_base64_basic()
    test_bytes_to_base64_empty()
    test_bytes_to_base64_hex_input()
    test_bytes_to_base64_padding()
    test_bytes_to_base64_non_ascii()
    print("All tests passed.")
    
def test_hex_to_bytes():
    assert "I\\\'m killing your brain like a poisonous mushroom" in str(hex_to_bytes("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")), "AHHAH"

def test_hamming():
    arg1 = b"this is a test"
    arg2 = b"wokka wokka!!!"
    assert hamming_distance(arg1, arg2) == 37, "function hamming_distance is borken!"
    print("hamming_distance works!")

def test_base64_to_bytes():
    assert b"Man" == base64_to_bytes("TWFu"), "Failed for 'Man'"
    assert b"Ma" == base64_to_bytes("TWE="), "Failed for 'Ma'"
    assert b"M" == base64_to_bytes("TQ=="), "Failed for 'M'"
    assert b"any carnal pleasure." == base64_to_bytes("YW55IGNhcm5hbCBwbGVhc3VyZS4="), "Failed for 'any carnal pleasure.'"
    print("base64_to_bytes works!")

def test_pkcs_pad():
    assert pkcs_pad(b"YELLOW SUBMARINE", 20) == b"YELLOW SUBMARINE\x04\x04\x04\x04"
    print("pkcs_pad test passed")
