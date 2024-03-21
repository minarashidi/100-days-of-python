alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text_input = input("Type your message:\n").lower()
shift_number_input = int(input("Type your shift number:\n"))


def caesar(text, shift_number):
    output_text = ""
    if direction == "decode":
        shift_number *= -1
    for char in text:
        output_text += alphabet[alphabet.index(char) + shift_number]
    print(f"The encoded text is {output_text}")


caesar(text_input, shift_number_input)
