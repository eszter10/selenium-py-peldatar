x = 0

#szám beírását kérem a felhasználótól amíg 10-nél kisebbet ír, számmá alakítom
while True:
    my_x = int(input())
    if my_x >= 10:
        break
#a beírt számokat összeadom
    x += my_x

#az összeget kiiratom
print(x)










