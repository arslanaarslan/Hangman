word = list(input())

is_palindrome = True

start = 0
end = -1

while start <= len(word) // 2:

    if word[start] != word[end]:
        is_palindrome = False
        break
    
    start += 1
    end -= 1
        
if is_palindrome:
    print("Palindrome")
else:
    print("Not palindrome")
