import AES as aes       # Import AES to use it
import OFB as ofb       # Import OFB to test it
from copy import copy   # It is used to copy the array


def print_separator_short():
    print("-----------------------------------------------------------------------------------")


def print_separator_long():
    print("=======================================================================================================================================")


def OFB_test(key, text):
    iv_enc_val = ofb.generate_initialization_vector()
    iv_dec_val = copy(iv_enc_val)

    cipher_text_arr, added_item_count = ofb.OFB_encryption(key, text, iv_enc_val)
    enc_str_arr = []
    for cipher_text in cipher_text_arr:
        enc_str_arr.append(aes.translate_hex_into_str(cipher_text))
    encrypt_text_str = ofb.merge_strings_without_remove_item(enc_str_arr)
    resolved_text_val = ofb.OFB_decryption(key, cipher_text_arr, iv_dec_val, added_item_count)

    print("Key : \'{}\'".format(key))
    print("Message Text : \'{}\'".format(text))
    print("Length of Text :", len(text))
    print("Encrypted Text:", encrypt_text_str)
    print("Length of Encrypted Text :", len(encrypt_text_str))
    print("Resolved Text : \'{}\'".format(resolved_text_val))
    print("Length of Resolved Text :", len(resolved_text_val))


if __name__ == '__main__':
    print_separator_short()
    print("Example of AES encryption and decryption with version of OFB")
    print("128 bit key and N bit message")
    print("There are two examples of keys and messages")
    print_separator_short()

    KEYS = ["Thats my Kung Fu", "AliHaydar KURBAN"]
    TEXTS = ["You can encrypt the messages has longer length then 16 bytes with CBC",
             "If the message is not multiple of 16 then add some constant item to message and make it multiple of 16"]

    for test_num in range(2):
        print_separator_long()
        OFB_test(KEYS[test_num], TEXTS[test_num])
        print_separator_long()