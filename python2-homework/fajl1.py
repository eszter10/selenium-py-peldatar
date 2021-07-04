#with open("adat.txt", "r") as f:
#    result = f.readlines()

#print(result)

nyit = open("adat.txt")
for sor in nyit:
    print(sor.strip() + " ", end="")
nyit.close()
print('')
