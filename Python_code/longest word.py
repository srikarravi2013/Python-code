def find_longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)


text = "I love learning Python"
print(find_longest_word(text))  