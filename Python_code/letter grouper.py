def group_by_first_letter(words):
    grouped = {}
    for word in words:
        if word:  # Check for empty strings
            key = word[0].lower()
            grouped.setdefault(key, []).append(word)
    return grouped


words = ["apple", "ant", "banana", "bat"]
print(group_by_first_letter(words))