#kódok és a hozzátartozó betűk kiiratása
#for i in range(26):
#    szam = i + 97
#    print(szam, chr(szam))

#sorokba rendezés
#print(szam, chr(szam,),szam, chr(szam,),szam, chr(szam,))
abc = ('abcdefghijklmnopqrstuvwxyz')
sor = ''
for i in range (0,len(abc)):
    betu = abc [i]
    if i > 0 and (i % 5) == 0 :
        print(sor)
        sor = ''
    sor += '\t'+betu+' '+str(ord(betu))
print(sor)
