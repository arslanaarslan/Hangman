value = int(input())

for i in range(value):
    string = "#" * (i * 2 + 1)
    print(string.center(value * 2 - 1))
