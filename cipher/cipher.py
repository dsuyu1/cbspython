import string 

def caeser_encrypt(message, key):
    shift = key % 26
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

    encryted_message = message.lower().translate(cipher)

    return encryted_message

def caeser_decrypt(encrypted_message, key):
    shift = 26 - (key % 26)
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

    message = encrypted_message.translate(cipher)
    return message

message = "Hello World!"
key = 3

encrypted_message = caeser_encrypt(message, key)
print(f'Encrypted message: {encrypted_message}')

decrypted_message = caeser_decrypt(encrypted_message, key)
print(f'Decrypted message: {decrypted_message}')
