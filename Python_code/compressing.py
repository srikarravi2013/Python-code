x = 'aabbba'

current_char = ""
count = 0
compressed = "" 

for char in x:
    if char == current_char:
        count += 1
    else:
        if count > 0 and current_char != "":
            compressed += current_char + str(count)
        
        current_char = char
        count = 1
        
if count > 0 and current_char != "":
    compressed += current_char + str(count)

print(compressed)