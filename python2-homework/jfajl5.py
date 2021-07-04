with open("adat.txt", 'r') as data:
    with open("masik.txt", 'w') as out:
        out.write(data.read())