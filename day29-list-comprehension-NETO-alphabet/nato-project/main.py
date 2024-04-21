import pandas as pd

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
letter_code_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
# print(letter_code_dict)

word = input("Enter a word: ").upper()
result = [letter_code_dict[letter] for letter in word]
print(result)
