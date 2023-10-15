d = {}

with open("en-ru.txt") as f:
    for line in f:
        eng = line.split("-")[0].strip()
        rus = line.split("-")[1].strip().split(',')
        for i in rus:
            i = i.strip()
            if i in d.keys():
                d[i] = d[i] + ", " + eng
            else:
                d[i] = eng

with open("ru-en.txt", "w") as file:
    for i in sorted(d.keys()):
        file.writelines(f"{i} - {d[i]}\n")

