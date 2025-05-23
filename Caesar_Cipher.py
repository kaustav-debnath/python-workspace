def encrypt_text(input, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_text=''
    for char in input.lower():
        index = alphabet.find(char)
        if( not char.isalpha()):
            new_text += char
        else:
            new_text += alphabet[(index+shift) % len(alphabet)]
        
    return new_text

text = 'Hello Worldzy'
shift = 3
encrypted = encrypt_text(text, shift)
print('input text:',text,'\nencrypted text:',encrypted)
decrypted = encrypt_text(encrypted, -3)
print('input text:',encrypted,'\nencrypted text:',decrypted)