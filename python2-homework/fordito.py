#létrehozok egy listát
my_list = []

#felhasználó tól kérek számokat amíg nem ír 0-t, listába rendezem
while True:
    my_x = int(input("Írj be egy számot!"))
    if my_x == 0:
        break
    my_list.append(my_x)

#megfordítom a számok sorrendjét
my_list2 = my_list[::-1]

#kiiratom a fordított listát
print(my_list2)




