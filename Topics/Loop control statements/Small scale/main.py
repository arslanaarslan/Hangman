float_values = []

while True:
    value = input()
    
    if value == ".":
        break
    else:
        float_values.append(float(value))
        
print(min(float_values))
