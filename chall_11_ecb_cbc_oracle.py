from set_01_utils import ecb_encrypt, ecb_decrypt
from set_02_utils import cbc_encrypt, cbc_decrypt, pkcs_pad
import os
betty = b"""Betty, I really hope you're on my side
I really hope you get it
Betty, I really hope you're on my side
I really hope you get it

I tried to get my shit together
Now you want a break
'Cause I'm not ready for forever
I wonder if you hate me
I bet I hate me more
Oh, trust me, I'd give anything
To tell you that I'm sure

I don't wanna lose you
I'm just thinking out loud

So could you call me back, hello, hello?
I'm tryna work this out
I know your friends say
"When you know, you know"
I just don't know right now
So could you call me back, hello, hello?
I'm tryna work this out
I know your friends say
"When you know, you know"
I just don't know right now
Betty, I really hope you're on my side
I really hope you get it

Next time you see your folks at dinner
Just ask your Mom to please
Stop pointing at your finger
I know she calls me "son" now
Your dad, he calls me "kid"
I'm sorry, I'm not man enough
To face 'em both like this

Don't read my last two messages
I barely slept an hour

So could you call me back, hello, hello?
I'm tryna work this out
I know your friends say
"When you know, you know"
I just don't know right now
Or could you give me just a year or so
To straighten out my head?
I know your friends say
"When you know you know"
So maybe, maybe, I'll know then
Betty, I really hope you're on my side
I really hope you get it
Betty, I truly hope you're on my side
I really hope you get it

I don't know
I don't know
Betty, I really hope you're on my side
I really hope you get it
Betty, I really hope you're on my side
I really hope you get it
Betty, I really hope you get it right
I just don't know right now
Betty, I really hope you get it right
I just don't know right now
Betty, I really hope you get it right
"""
def black_box(message: bytes) -> "tuple[bytes,bytes,bytes]":
    message = pkcs_pad(message, 16)
    key = os.urandom(16)
    if os.urandom(1)[0] > 128:
        # Encrypt with CBC
        iv = os.urandom(16)
        return (cbc_encrypt(message, key, iv), key, iv)
    else:
        # Encrypt with ECB
        return (ecb_encrypt(message, key), key, b"")
# print(black_box(betty))
def test_black_box():
    test_message = pkcs_pad(b"I know your friends say\n\"When you know, you know\"\nI just don't know right now", 16)
    black_box_output = black_box(test_message)
    while len(black_box_output[2]) != 0:
        black_box_output = black_box(test_message)
    assert ecb_decrypt(black_box_output[0], black_box_output[1]) == test_message
    while len(black_box_output[2]) == 0:
        black_box_output = black_box(test_message)
    assert cbc_decrypt(black_box_output[0], black_box_output[1], black_box_output[2]) == test_message
    print("Black box works")
if __name__ == "__main__":
    test_black_box()
    
def oracle():