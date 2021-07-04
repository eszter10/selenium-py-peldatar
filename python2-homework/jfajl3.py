with open("adat.txt", 'r') as data:
    with open("masik.txt", 'w') as out:
        lines = data.readlines()
        filtered_lines = []
        for line in lines:
            filtered_lines.append(line.replace('\n', ''))
        out.write(" ".join(filtered_lines))