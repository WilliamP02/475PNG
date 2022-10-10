# William Pridgen
# CSC 475
# assignment 2
# uses given code from https://www.geeksforgeeks.org/pseudo-random-number-generator-prng/
#10/9/22

import random
import time


def ByEncrypt(message):
    """

    :param message: The message (str) to be encrypted
    :return: returns a list with the orignal message, the Psuedo Random Sequence and the Final encrypted message
    """
    random.seed(int(time.time()))
    en_message = message.encode()
    byte_array = bytearray(en_message)
    m_len = len(byte_array)
    pseudo_seq = bytearray(random.randbytes(m_len))
    final_message = bytes(b1 ^ b2 for (b1, b2) in zip(byte_array, pseudo_seq))
    return [final_message, message, pseudo_seq]


def ByDencrypt(message, key):
    """

    :param message: The message (str) to be decrypted
    :param key: The key used to encrypt
    :return: A string of the decrypted message
    """
    dec = bytes(b1 ^ b2 for (b1, b2) in zip(message, key))
    return str(dec)


choice = input("Encrypt (E) or decrypt (D): ")
if choice == 'E':
    message2 = (input("Welcome, please input the message you wish to encrypt:"))
    result = ByEncrypt(message2)
    print("Original message:", result[1])
    print("Pseudo Random Sequence:", result[2])
    print("Final Messsage:", result[0])
elif choice == 'D':
    message2 = (input("Welcome, please input the message you wish to decrypt:"))
    key = input("Key:")
    print(ByDencrypt(message2, key))
else:
    print("unknown request, please try again")
