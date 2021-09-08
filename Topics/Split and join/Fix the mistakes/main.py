text = input()
words = text.split()
for word in words:
    # finish the code here
    string = word.lower()
    
    if string[0] in ("h", "w") and string[-1] in ("m", "g", "/", ":"):
        print(word)
