def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase for comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)


word1 = "listen"
word2 = "silent"
print(is_anagram(word1, word2))