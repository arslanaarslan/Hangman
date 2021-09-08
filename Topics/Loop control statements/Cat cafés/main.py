cafe_names = []
number_of_cats = []

while True:
    word = input()
    
    if word == "MEOW":
        break
    else:
        name_and_number = word.split()
        cafe_names.append(name_and_number[0])
        number_of_cats.append(int(name_and_number[1]))

index_of_max = 0
max_value = 0       

for index, number in enumerate(number_of_cats):
    if number > max_value:
        max_value = number
        index_of_max = index
        
print(cafe_names[index_of_max])
