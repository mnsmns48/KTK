tarif_l = []
tarif = open('ktk_base_tarif.txt')
for line in tarif:
    tarif_l.append(line.strip())
    locals()[line] = {}


for i in range(len(tarif_l)):
    line = tarif_l[i]
    globals()[line] = {}
print(unlim)

unlim.append()