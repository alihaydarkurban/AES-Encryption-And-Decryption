import AES as aes       # Import AES to implement OFB
import random           # It is used to generate random integer

WORD_LENGTH = 4         # Length of matrix
SIZE = 16               # Length of the texts


# It generates a random initialization vector with size 16
def generate_initialization_vector():
    in_vector = [0 for x in range(SIZE)]
    for i in range(SIZE):
        in_vector[i] = random.randint(1, 101)

    return in_vector


# It splits the text 16 bytes by 16 bytes
# It adds 'X' to the text if it is not multiple of 16
def split_plain_text(string):
    plain_text_arr = [string[i:i + SIZE] for i in range(0, len(string), SIZE)]
    size_of_last_part = len(plain_text_arr[len(plain_text_arr) - 1])
    added_item_count = SIZE - size_of_last_part
    last_item_index = len(plain_text_arr) - 1
    for i in range(added_item_count):
        plain_text_arr[last_item_index] = plain_text_arr[last_item_index] + 'X'

    return plain_text_arr, added_item_count


# It takes a hex string matrix and converts it to a hex string array
def reverse_matrix_to_hex_string_arr(matrix):
    arr = ['' for x in range(SIZE)]
    index = 0
    for i in range(WORD_LENGTH):
        for j in range(WORD_LENGTH):
            arr[index] = matrix[j][i]
            index = index + 1
    return arr


# It converts the string array to string
# It remove the 'X's if it was added
def merge_strings(str_arr, remove_count):
    text = ""
    if remove_count == 0:
        for string in str_arr:
            text = text + string
    else:
        final = str_arr.pop(len(str_arr) - 1)
        for string in str_arr:
            text = text + string
        for i in range(SIZE - remove_count):
            text = text + final[i]

    return text


# It converts the string array to string
# It does not remove the 'X's
def merge_strings_without_remove_item(str_arr):
    text = ""
    for string in str_arr:
        text = text + string
    return text


# It is encryption operation for the OFB
# It takes the main key, message and the initialization vector
# It returns count of added 'X's and encrypted message as hex string 2d array
def OFB_encryption(key_val, text_val, iv_enc_val):
    plain_text_arr, added_item_count = split_plain_text(text_val)
    key_in_hex = aes.translate_string_into_hex_str(key_val)
    all_round_key = aes.find_all_round_keys(key_in_hex)
    cipher_text_arr = []


    hex_iv_enc = aes.make_int_arr_to_hex(iv_enc_val)
    current_enc_output = aes.encrypt(hex_iv_enc, all_round_key)

    hex_plain_text = aes.translate_string_into_hex_str(plain_text_arr[0])
    hex_plain_text_matrix = aes.generate_4x4_matrix(hex_plain_text)
    current_enc_output_matrix = aes.generate_4x4_matrix(current_enc_output)
    cipher_text_matrix = aes.add_round_key(current_enc_output_matrix, hex_plain_text_matrix)
    cipher_text = reverse_matrix_to_hex_string_arr(cipher_text_matrix)
    cipher_text_arr.append(cipher_text)

    for i in range(1, len(plain_text_arr)):
        current_enc_output = aes.encrypt(current_enc_output, all_round_key)
        hex_plain_text = aes.translate_string_into_hex_str(plain_text_arr[i])
        hex_plain_text_matrix = aes.generate_4x4_matrix(hex_plain_text)
        current_enc_output_matrix = aes.generate_4x4_matrix(current_enc_output)
        cipher_text_matrix = aes.add_round_key(current_enc_output_matrix, hex_plain_text_matrix)
        cipher_text = reverse_matrix_to_hex_string_arr(cipher_text_matrix)
        cipher_text_arr.append(cipher_text)

    return cipher_text_arr, added_item_count


# It is decryption operation for the CBC
# It takes the main key, encrypted message, initialization vector and count of added 'X's to remove
# It returns count of added 'X's and encrypted message as hex string 2d array
def OFB_decryption(key_val, cipher_text_arr, iv_dec_val, remove_count):
    key_in_hex = aes.translate_string_into_hex_str(key_val)
    all_round_key = aes.find_all_round_keys(key_in_hex)
    plain_text_arr = []

    hex_iv_dec = aes.make_int_arr_to_hex(iv_dec_val)
    current_enc_output = aes.encrypt(hex_iv_dec, all_round_key)

    current_enc_output_matrix = aes.generate_4x4_matrix(current_enc_output)
    cipher_text_matrix = aes.generate_4x4_matrix(cipher_text_arr[0])
    plain_text_matrix = aes.add_round_key(current_enc_output_matrix, cipher_text_matrix)
    plain_text_hex = reverse_matrix_to_hex_string_arr(plain_text_matrix)
    plain_text_str = aes.translate_hex_into_str(plain_text_hex)
    plain_text_arr.append(plain_text_str)

    for i in range(1, len(cipher_text_arr)):
        current_enc_output = aes.encrypt(current_enc_output, all_round_key)
        current_enc_output_matrix = aes.generate_4x4_matrix(current_enc_output)
        cipher_text_matrix = aes.generate_4x4_matrix(cipher_text_arr[i])
        plain_text_matrix = aes.add_round_key(current_enc_output_matrix, cipher_text_matrix)
        plain_text_hex = reverse_matrix_to_hex_string_arr(plain_text_matrix)
        plain_text_str = aes.translate_hex_into_str(plain_text_hex)
        plain_text_arr.append(plain_text_str)

    resolved_text_val = merge_strings(plain_text_arr, remove_count)

    return resolved_text_val


