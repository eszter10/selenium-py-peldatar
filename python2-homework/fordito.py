my_list = []

while True:
    my_x = int(input("Írj be egy számot!"))
    if my_x == 0:
        break
    my_list.append(my_x)

my_list2 = my_list[::-1]

print(my_list2)




