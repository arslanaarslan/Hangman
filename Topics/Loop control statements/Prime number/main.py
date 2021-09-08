number = int(input())

is_prime = False

divider = 2

while divider <= number:
    
    if number == divider:
        is_prime = True
        break
        
    if number == 2:
        is_prime = True
        break
        
    if number % divider == 0:
        break
    
    divider += 1
    
if is_prime:
    print("This number is prime")
else:
    print("This number is not prime")
