r = open("IDS", "r")
w = open("ID2", "w")
final = {}

lines = r.read().splitlines()

for line in lines:
    linelist = (line[:10] + "?" + line[10:46] + "?" + line[46:58] + "?" + line[58:]).split("?")
    for s in linelist:
        linelist[linelist.index(s)] = s.strip()
    if len(linelist) < 2:
        lines.remove(line)
    else:
        final.update({linelist[1]: linelist[0]})
print(final)