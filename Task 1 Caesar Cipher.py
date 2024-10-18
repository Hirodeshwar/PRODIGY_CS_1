def encrypt(text, shift):
    result = ""
    

    for i in range(len(text)):
        char = text[i]
        
    
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
    
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        else:
            result += char
    
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)



choice = input("Do you want to (E)ncrypt or (D)ecrypt?: ").lower()

if choice == 'e':
    message = input("Enter message to encrypt: ")
    shift = int(input("Enter shift value: "))
    print(f"Encrypted message: {encrypt(message, shift)}")
    
elif choice == 'd':
    message = input("Enter message to decrypt: ")
    shift = int(input("Enter shift value: "))
    print(f"Decrypted message: {decrypt(message, shift)}")

else:
    print("Invalid choice")
