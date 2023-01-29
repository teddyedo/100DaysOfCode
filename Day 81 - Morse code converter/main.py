import morse_code

while True:

    encrypt_or_decrypt = input("Do you want to encrypt or decrypt your "
                               "string? (E or D): ")

    if encrypt_or_decrypt == "E":
        text = input("Write the text you want to encrypt: ")
        print(f"This is your encrypted message: {morse_code.encrypt(text)}")

    elif encrypt_or_decrypt == "D":
        text = input("Write the text you want to decrypt: ")
        print(f"This is your decrypted message: {morse_code.decrypt(text)}")

    else:
        print("Invalid command. Retry.")

