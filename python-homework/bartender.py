# adatok bekérérse
x = int(input("Hány éves vagy?"))
y = input("Írd be a kért italt: sör vagy kóla")

# 18 év alatti nem kap sört
if x < 18 and y = 'sör':
    print("Túl fiatal vagy:(")
# 18 év feletti kap sört
elif x >= 18:
    print("Parancsoljon, a söre")
# 60 év feletti figyelmeztetése
if x > 60 and y ="kóla":
    print("A koffein megemelheti a vérnyomását.")
# 60 év alatti kap kólát
elif x >= 60:
    print("Parancsoljon, a kólája.")
# figyelmeztetés, ha más italt kér
if y != "sör" and y != "kóla":
    print("Csak sör és kóla van.")
