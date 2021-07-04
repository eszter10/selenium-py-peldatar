with open("adat.txt", 'r') as data:
    with open("masik.txt", 'w') as out:
        lines = data.readlines()
        for line in lines:
            out.write(line)