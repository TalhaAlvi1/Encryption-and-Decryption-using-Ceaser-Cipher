# **Encryption and Decryption using Caesar Cipher**

This is a simple Java program that implements the Caesar Cipher technique to encrypt and decrypt messages. Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted a fixed number of places down or up the alphabet.

# Algorithm for the Caesar Cipher Program:
 Start
 
 Input Step:
 
Prompt the user to enter a string (currently asks for less than 10 characters).

 Initialize an empty string called result to store the final encrypted output.
 
·  Loop through each character in the input string:

·  For each character ch in the string, do the following:

a. Check if ch is a lowercase letter (between 'a' and 'z'):

Shift ch forward by 3 positions in the ASCII table (ch + 3).

If the shifted character goes beyond 'z' (i.e., shifted value > 'z'):

Wrap it around by subtracting 26 (i.e., shiftedChar = shiftedChar - 26).

Append the shifted character to result.

b. Check if ch is an uppercase letter (between 'A' and 'Z'):

Shift ch forward by 3 positions in the ASCII table (ch + 3).

If the shifted character goes beyond 'Z' (i.e., shifted value > 'Z'):

Wrap it around by subtracting 26 (i.e., shiftedChar = shiftedChar - 26).

Append the shifted character to result.
·  Output the Encrypted String:

·  Once all characters have been processed, print the result string as the final encrypted output.

·  End

# Explanation
User Input:

The program asks the user to input a string.

Character Shifting:

The program checks if the character is a lowercase letter ('a' to 'z'), and shifts it by 3 positions in the ASCII table.

Similarly, for uppercase letters ('A' to 'Z'), it shifts the character by 3.

If the shifted character exceeds the alphabetic range ('z' for lowercase or 'Z' for uppercase), the program wraps around to the start of the alphabet by subtracting 26 (which brings it back to the proper range).

Output:

After processing all characters, the final encrypted string is printed to the console.

# **Features****

**Encryption:** Encrypts a message by shifting each letter by a specified number of positions.

**Decryption:** Decrypts a message by shifting each letter back to its original position.

# **How to Use**

**Run the Program:**

Open the program in your favorite Java IDE or use the command line.
Input the text you want to encrypt or decrypt.
Specify the shift value.
**Example:**

Plaintext: HELLO

Shift: 3

Encrypted Text: KHOOR

# **Technologies Used**

Python
