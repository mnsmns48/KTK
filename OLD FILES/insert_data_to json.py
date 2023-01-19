import json

#
# with open('ktk.json') as f:
#     templates = json.load(f)

sales = {}
surname = 'Фамилия'
print(surname)
sales['95434'] = {surname: input()}
name = 'Имя'
print(name)
sales['95434'].update({name: input()})
patronymic = 'Отчество'
print(patronymic)
sales['95434'].update({patronymic: input()})
series_passport = 'Серия паспорта'
print(series_passport)
sales['95434'].update({series_passport: input()})
number_passport = 'Номер паспорта'
print(number_passport)
sales['95434'].update({number_passport: input()})
department_passport = 'Кем выдан паспорт'
print(department_passport)
sales['95434'].update({department_passport: input()})
date_passport = 'Дата выдачи паспорта (через пробел)'
print(date_passport)
sales['95434'].update({date_passport: input()})
date_birth = 'Дата рождения (через пробел)'
print(date_birth)
sales['95434'].update({date_birth: input()})
place_birth = 'Место рождения'
print(place_birth)
sales['95434'].update({place_birth: input()})
region = 'Регион / Область / Республика'
print(region)
sales['95434'].update({region: input()})
adress = 'Населенный пункт и улица'
print(adress)
sales['95434'].update({adress: input()})
house_flat = 'дом и квартира (через пробел)'
print(house_flat)
sales['95434'].update({house_flat: input()})
number = '95434'
contract = json.dumps(sales, indent=2)
with open(f"Sales/+797840{number}.json", 'w') as file:
    file.write(contract)
