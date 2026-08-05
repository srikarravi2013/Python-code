line_count = 0
word_count = 0
char_count = 0
path = input('what is your file path:')


with open(path, 'r') as file:
    for line in file:
        line_count += 1
        word_count += len(line.split())
        char_count += len(line)

print("Lines:", line_count)
print("Words:", word_count)
print("Characters:", char_count)