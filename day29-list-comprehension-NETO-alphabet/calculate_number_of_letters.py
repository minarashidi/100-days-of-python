sentence = input("Enter a sentence: ")
words = sentence.split()
print(words)

word_letters = {word: len(word) for word in words}
print(word_letters)
