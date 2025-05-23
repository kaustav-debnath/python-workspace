# This program is used to create an encryption and decryption program using Caesar Cipher
# The direction parameter tells us if we are gonna encrypt/decrypt the message


def vigenere(message, key, direction=1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''
    key_index = 0

    for char in message.lower():
        
        if not char.isalpha():
            final_message += char
        else:
            # find the right char to encode/decode
            key_char = key[key_index % len(key)]#p from key
            key_index+=1

            #Define the offset and the encrypted/decrypted text
            offset = alphabet.index(key_char)#position of key_char in alphabet = 15,24,19
            index = alphabet.find(char) #find the position of char in alphabet = 7,4,11
            new_index = (index + offset * direction) % len(alphabet) # (7 + 15*1) % 26 = 22
            # print(char, index, offset, direction, alphabet[new_index])
            final_message += alphabet[new_index]
            
    return final_message

text ='Hello World'
custom_key = 'python'

def encrypt(message, key):
    return vigenere(message, key)           
def decrypt(message, key):
    return vigenere(message, key, -1)

encryption = encrypt(text, custom_key)
print(encryption)
decryption = decrypt(encryption, custom_key)
print(decryption)