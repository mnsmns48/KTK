import json

with open('ktk.json', "r", encoding="utf-8") as f:
    templates = json.load(f)
    f.close()

tariff, number_list = [], []
for i in templates:
    tariff.append(i)

for i in range(len(tariff)):
    for k, v in templates[tariff[i]].items():
        number_list.append(k)


def big_dicts():
    big_dict = []
    with open('ktk.json', "r", encoding="utf-8") as f:
        templates = json.load(f)
        f.close()
    for i in range(len(tariff)):
        id_from_json = templates[tariff[i]]
        for k, v in id_from_json.items():
            big_dict.append(k)
    return big_dict


big_dict = big_dicts()
