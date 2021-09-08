guest_list = []

guest_name = input()

while guest_name != ".":
    guest_list.append(guest_name)
    guest_name = input()
    
print(guest_list)
print(len(guest_list))
