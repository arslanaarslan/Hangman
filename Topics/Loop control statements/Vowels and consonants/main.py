text = list(input())

for character in text:
    if character in "aeiou":
        print("vowel")
    elif character in "bcdfghjklmnpqrstvwxyz":
        print("consonant")
    else:
        break
