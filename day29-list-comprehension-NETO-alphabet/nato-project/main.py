import pandas as pd

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
print(phonetic_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        result = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, you need to enter only letters in the alphabet")
        generate_phonetic()
    else:
        print(result)


print(generate_phonetic())
