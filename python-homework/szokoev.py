def foo(x):
    print(x)

x = int(input())

if x % 4 == 0 and x % 400 == 0:
    print("Szökőév")
elif x % 4 != 0:
    print("Nem szökőév")
else:
    print("Nem szökőév")

