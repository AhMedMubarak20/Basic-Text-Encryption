def caesar_cipher(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_text += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

message = input("Enter the message to encrypt: ")
shift_amount = int(input("Enter the shift amount (1-25): "))
encrypted_message = caesar_cipher(message, shift_amount)
print("Encrypted message:", encrypted_message)
