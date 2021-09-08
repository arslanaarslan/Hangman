scores = input().split()
# put your python code here

number_of_true = 0
number_of_false = 0

for score in scores:
    if score == 'I':
        number_of_false += 1
        if number_of_false == 3:
            print("Game over")
            break
    else:
        number_of_true += 1
else:
    print("You won")

print(number_of_true)
