import tkinter as tk
from tkinter import messagebox

# Encryption function
def encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

# Decryption function
def decrypt(text, shift):
    return encrypt(text, -shift)

# Encrypt Button Function
def encrypt_text():
    text = text_entry.get()
    shift = shift_entry.get()
    
    if not shift.isdigit():
        messagebox.showerror("Invalid input", "Shift must be a number")
        return
    
    shift = int(shift)
    encrypted = encrypt(text, shift)
    result_label.config(text=f"Encrypted Text: {encrypted}")

# Decrypt Button Function
def decrypt_text():
    text = text_entry.get()
    shift = shift_entry.get()
    
    if not shift.isdigit():
        messagebox.showerror("Invalid input", "Shift must be a number")
        return
    
    shift = int(shift)
    decrypted = decrypt(text, shift)
    result_label.config(text=f"Decrypted Text: {decrypted}")

# Initialize the tkinter window
root = tk.Tk()
root.title("Caesar Cipher")

# Labels and Entries
text_label = tk.Label(root, text="Enter Text:")
text_label.pack()

text_entry = tk.Entry(root, width=50)
text_entry.pack()

shift_label = tk.Label(root, text="Enter Shift:")
shift_label.pack()

shift_entry = tk.Entry(root, width=10)
shift_entry.pack()

# Buttons
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Start the tkinter event loop
root.mainloop()
