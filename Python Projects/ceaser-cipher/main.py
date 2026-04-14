alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# input("Type 'E' to encrypt and type 'D' to decrypt:\n ").upper()
message = input("Enter your message: ").upper()
shift_number = int(input("Enter the shift number: "))

def encrypt_str(user_message, user_shift_number):
    encrypted_messgae = ''
    print(user_message)
    for char in user_message:
        position = alphabet.index(char)
        
        shifted_position = position + user_shift_number
        new_char = alphabet[shifted_position]
        encrypted_messgae += new_char
    return encrypted_messgae

        # print(f"{char} - {position} - {shifted_position}")


print(encrypt_str(message, shift_number))