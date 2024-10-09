def encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isupper():
            result += chr((ord(char)+shift-65)%26+65)
        
        elif char.islower():
            result += chr((ord(char)+shift-97)%26+97)
        else:
            result += char
    return result
    
def decrypt(text, shift):
    return encrypt(text, -shift)
        
text = input("ENter the text: ")
shift = int(input("Enter the shift (key): "))
    
encrypted_text = encrypt(text, shift)
print(f"Encryted Text: {encrypted_text}")
    
decrypted_text = decrypt(encrypted_text, shift)
print(f"Decrypted Text : {decrypted_text}")
        