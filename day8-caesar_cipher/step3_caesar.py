from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(text, shift_amount, cipher_direction):
    output_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in text:
        # TODO-3: Preserve the the number/symbol/space when the text is encoded/decoded
        # e.g. start_text = "meet me at 3 end_text = "•••• •• •• 3"
        if char in alphabet:
            output_text += alphabet[alphabet.index(char) + shift_amount]
        else:
            output_text += char
    print(f"Here's the {cipher_direction}d result: {output_text}")


# TODO-4: Able to restart the cipher program
should_end = False
while not should_end:
    direction_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text_input = input("Type your message:\n").lower()
    shift_number_input = int(input("Type your shift number:\n"))
    # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    shift = shift_number_input % 26
    caesar(text_input, shift, direction_input)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if restart == "no":
        should_end = True
        print("Goodbye!")
