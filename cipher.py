letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(text, shift):
    result = ""
    for char in text:
        if char in letters:
            index = letters.index(char)
            new_index = (index + shift) % 26
            result += letters[new_index]
        else:
            result += char
    return result

text = input("Text to cipher: ")
shift = int(input("Shift value (1-25): "))

if 1 <= shift <= 25:
    ciphered_text = cipher(text, shift)
    print("Ciphered text:", ciphered_text)