alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text_input = input("Type your message:\n").lower()
shift_number_input = input("Type your shift number:\n")


def encrypt(plain_text, shift_number):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            cipher_text += alphabet[alphabet.index(char) + int(shift_number)]
    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, shift_number):
    plain_text = ""
    for char in cipher_text:
        plain_text += alphabet[alphabet.index(char) - int(shift_number)]
    print(f"The decoded text is {plain_text}")


if direction == "encode":
    encrypt(text_input, shift_number_input)
elif direction == "decode":
    decrypt(text_input, shift_number_input)
