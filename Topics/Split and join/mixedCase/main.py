words = input().split()

for i, word in enumerate(words):
    if i == 0:
        words[i] = word.lower()
    else:
        words[i] = word.capitalize()
        
result = "".join(words)

print(result)
