import json

graphite = {}
orange = {}
unlim = {}
universal = {}
white = {}
blue = {}

tarif_list, keys, id = [], [], []
tarif = open('ktk_base_tarif.txt', encoding='utf-8')
for line in tarif:
    tarif_list.append(line.replace('\n', ''))

k = open('ktk_base_number.txt', encoding='utf-8')
for line in k:
    keys.append(line.replace('\n', ''))

i = open('ktk_base_id.txt', encoding='utf-8')
for line in i:
    id.append(line.replace('\n', ''))


def create_dict(name, a, b, i):
    name[i] = dict(zip(keys[a:b], id[a:b]))
    return name


ktk = (create_dict(graphite, 0, 17, tarif_list[0])
       | create_dict(unlim, 18, 25, tarif_list[1])
       | create_dict(universal, 26, 31, tarif_list[2])
       | create_dict(white, 32, 40, tarif_list[3])
       | create_dict(blue, 41, 44, tarif_list[4])
       | create_dict(orange, 45, 52, tarif_list[5])
       )

ktk_json = json.dumps(ktk, indent=2)
with open('ktk_2.json', 'w', encoding="utf-8") as file:
    file.write(ktk_json)