from tkinter import Tk, Entry, Button, Label, Grid, Text, PhotoImage
from tkinter.ttk import Combobox
import json
from load_data import templates, tariff, big_dicts
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime


data_contract = dict()


class Window:
    def __init__(self, width, height, title="NewApp", resizable=(False, False), icon=None):
        self.entry = None
        self.surname = None
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)
        self.face_image = PhotoImage(file='ico.png')
        self.root.iconphoto(False, self.face_image)
        self.root.configure(background='Grey')

    def draw_entry(self, background, justify, row, column, index, minsize):
        self.entry = Entry(self.root, background=background, justify=justify)
        self.entry.grid(row=row, column=column)
        self.entry.grid_columnconfigure(index, minsize=minsize)
        return self.entry

    def refresh(self):
        self.label.destroy()
        self.entry.destroy()
        self.tariff_combobox.destroy()
        self.run()

    def draw_button(self, text, command, row, column, index, minsize):
        self.button = Button(self.root, text=text, command=command)
        self.button.grid(row=row, column=column)
        self.button.grid_columnconfigure(index=index, minsize=minsize)

    def draw_label(self, text, row=0, column=0, stick="E", index=0, minsize=100):
        self.label = Label(self.root, text=text)
        self.label.grid(row=row, column=column, stick=stick)
        self.label.grid_columnconfigure(index, minsize=minsize)

    def draw_tariff_combobox(self, values, row, column, index, minsize):
        self.tariff_combobox = Combobox(self.root, values=values, state="readonly")
        self.tariff_combobox.grid(row=row, column=column)
        self.tariff_combobox.grid_columnconfigure(index=index, minsize=minsize)
        self.tariff_combobox.current(0)
        self.tariff_combobox.bind("<<ComboboxSelected>>", self.get_tariff)

    def draw_tariff_combobox_add(self, values, row, column, index, minsize):
        self.tariff_combobox = Combobox(self.root, values=values, state="readonly")
        self.tariff_combobox.grid(row=row, column=column)
        self.tariff_combobox.grid_columnconfigure(index=index, minsize=minsize)
        self.tariff_combobox.bind("<<ComboboxSelected>>", self.get_tariff_add)

    def get_tariff_add(self, event):
        global value_tariff_add
        value_tariff_add = self.tariff_combobox.get()

    def get_tariff(self, event):
        global value_tariff
        value_tariff = self.tariff_combobox.get()
        return self.draw_number_combobox(list(templates[value_tariff].keys()), 1, 0, 1, 20)

    def draw_number_combobox(self, values, row, column, index, minsize):
        self.number_combobox = Combobox(self.root, values=values, state="readonly")
        self.number_combobox.grid(row=row, column=column)
        self.number_combobox.grid_columnconfigure(index=index, minsize=minsize)
        self.number_combobox.bind("<<ComboboxSelected>>", self.get_id)

    def get_id(self, event):
        global value_number
        value_number = self.number_combobox.get()
        self.draw_label(templates[value_tariff][value_number], 2, 0, None, 2, 100)
        self.text = 'остаток сим карт по данному тарифу  ' + str(len(templates[value_tariff]))
        self.draw_label(self.text, 1, 1, "W", 1, 100)

    def insert_text(self, word, width, height, font_size):
        self.print_contract = ImageDraw.Draw(self.im)
        self.font = ImageFont.truetype('arialmt.ttf', size=font_size)
        self.print_contract.text((width, height), str(word), font=self.font, fill='#000000')

    def add_to_db(self):
        self.number_field = Text(width=25, height=15)
        self.number_field.grid(row=19, column=0)
        self.number_field.grid_columnconfigure(index=19, minsize=100)
        self.draw_tariff_combobox_add(tariff, 18, 1, 18, 70)
        self.id_field = Text(width=25, height=15)
        self.id_field.grid(row=19, column=1)
        self.id_field.grid_columnconfigure(index=19, minsize=100)
        self.draw_button("Внести номера", self.update_db, 18, 2, 18, 50)

    def update_db(self):
        self.numbers = self.number_field.get("1.0", "end").split()
        self.id = self.id_field.get("1.0", "end").split()
        with open('ktk.json', "r", encoding="utf-8") as f:
            templates_add = json.load(f)
        for i in range(len(self.numbers)):
            templates_add[value_tariff_add].update({self.numbers[i]: self.id[i]})
        ktk_json = json.dumps(templates_add, indent=2)
        with open('ktk.json', 'w') as file:
            file.write(ktk_json)
            file.close()
        self.label.destroy()
        self.tariff_combobox.destroy()
        self.root.update()
        self.draw_label(f'Добавлено в {value_tariff_add}', 20, 1, "W", 20, 200)
        self.draw_label('Всего сим карт     ' + str(len(big_dicts())), 0, 1, "W", 0, 70)
        self.run()


    def entry_text(self):
        self.surname = self.surname.get()
        self.name = self.name.get()
        self.patronymic = self.patronymic.get()
        self.date_birth = self.date_birth.get()
        self.place_birth = self.place_birth.get()
        self.passport_series = self.passport_series.get()
        self.passport_number = self.passport_number.get()
        self.passport_issued_by = self.passport_issued_by.get()
        self.passport_date = self.passport_date.get()
        self.region = self.region.get()
        self.town_street = self.town_street.get()
        self.house_appt = self.house_appt.get().split(" ")

        data_contract[value_number] = {"Фамилия": self.surname}
        data_contract[value_number].update({"Имя": self.name})
        data_contract[value_number].update({"Отчество": self.patronymic})
        data_contract[value_number].update({"Дата рождения": self.date_birth})
        data_contract[value_number].update({"Место рождения": self.place_birth})
        data_contract[value_number].update({"Серия паспорта": self.passport_series})
        data_contract[value_number].update({"Номер паспорта": self.passport_number})
        data_contract[value_number].update({"Кем выдан паспорт и код подразделения": self.passport_issued_by})
        data_contract[value_number].update({"Дата выдачи паспорта": self.passport_date})
        data_contract[value_number].update({"Регион прописки": self.region})
        data_contract[value_number].update({"Город и улица": self.town_street})
        data_contract[value_number].update({"Номер дома и квартира": " ".join(self.house_appt)})

        contract = json.dumps(data_contract, indent=2)
        with open(f'Contracts/JSON/{self.surname}_{value_number}.json', 'w') as file:
            file.write(contract)
        self.draw_label('Договор (json файл) успешно сохранен папке Contracts/JSON', 15, 1, "W", 15, 70)
        self.draw_button("Распечатать результат", self.print_image, 16, 0, 16, 50)
        self.draw_label('Договор готов к печати. Сохранен в папке /Contracts/', 16, 1, "W", 16, 100)
        self.draw_button("Удалить номер из БД", self.del_number, 17, 0, 17, 50)

    def print_image(self):
        self.im = Image.open('font.jpg')
        self.today = datetime.now()
        self.insert_text(self.today.day, 1320, 1372, 58)
        self.insert_text(self.today.month, 1555, 1372, 58)
        self.insert_text(self.today.year, 1795, 1372, 58)

        self.insert_text(self.surname, 220, 446, 58)
        self.insert_text(f'{self.surname} {self.name[0]}. {self.patronymic[0]}.', 769, 2112, 58)
        self.insert_text(self.name, 220, 521, 58)
        self.insert_text(self.patronymic, 220, 597, 58)

        self.insert_text("   ".join(self.passport_series), 302, 925, 58)
        self.insert_text("   ".join(self.passport_number), 302, 1000, 58)
        self.insert_text(self.passport_issued_by, 290, 1081, 30)
        self.insert_text("  ".join(self.passport_date), 75, 1198, 49)

        self.insert_text("  ".join(self.date_birth), 75, 1324, 49)
        self.insert_text(self.place_birth, 75, 1450, 40)

        self.insert_text(value_number, 1456, 103, 70)
        self.insert_text(templates[value_tariff][value_number], 1456, 205, 70)
        self.insert_text(value_tariff, 1651, 320, 58)

        self.insert_text(self.region, 1333, 522, 58)
        self.insert_text(self.town_street, 1333, 648, 58)
        self.insert_text(self.house_appt[0], 1345, 725, 58)
        try:
            self.insert_text(self.house_appt[1], 1914, 725, 58)
        except IndexError:
            pass
        self.draw_label("Выполнено. Ошибок нет", 17, 1, "W", 17, 100)
        self.im.save(f'Contracts/{self.surname}_{value_number}.jpg')

    def del_number(self):
        templates[value_tariff].pop(value_number)
        t_json = json.dumps(templates, indent=2)
        with open('ktk.json', "w") as file:
            file.write(t_json)
        self.draw_label(f'Номер {value_number} продан и удален из базы', 17, 1, "W", 17, 100)
        file.close()

    def run(self):
        self.draw_label('Всего сим карт     ' + str(len(big_dicts())), 0, 1, "W", 0, 70)
        self.draw_tariff_combobox(tariff, 0, 0, 0, 70)
        self.draw_label("Фамилия", 3, 1, "W", 3, 70)
        self.surname = self.draw_entry("White", "left", 3, 0, 3, 150)
        self.draw_label("Имя", 4, 1, "W", 4, 70)
        self.name = self.draw_entry("White", "left", 4, 0, 4, 150)
        self.draw_label("Отчество", 5, 1, "W", 5, 70)
        self.patronymic = self.draw_entry("White", "left", 5, 0, 5, 150)
        self.draw_label("Дата Рождения / 01 08 1985", 6, 1, "W", 6, 70)
        self.date_birth = self.draw_entry("White", "left", 6, 0, 6, 150)
        self.draw_label("Место рождения", 7, 1, "W", 7, 70)
        self.place_birth = self.draw_entry("White", "left", 7, 0, 7, 150)
        self.draw_label("Серия паспорта / без пробелов", 8, 1, "W", 8, 70)
        self.passport_series = self.draw_entry("White", "left", 8, 0, 8, 150)
        self.draw_label("Номер паспорта", 9, 1, "W", 9, 70)
        self.passport_number = self.draw_entry("White", "left", 9, 0, 9, 150)
        self.draw_label("Кем выдан и код подразделения", 10, 1, "W", 10, 70)
        self.passport_issued_by = self.draw_entry("White", "left", 10, 0, 10, 150)
        self.draw_label("Дата выдачи / 01 01 2023", 11, 1, "W", 1, 70)
        self.passport_date = self.draw_entry("White", "left", 11, 0, 1, 150)
        self.draw_label("Регион / область", 12, 1, "W", 12, 70)
        self.region = self.draw_entry("white", "left", 12, 0, 12, 150)
        self.draw_label("Населенный пункт и улица", 13, 1, "W", 13, 70)
        self.town_street = self.draw_entry("white", "left", 13, 0, 13, 150)
        self.draw_label("Номер дома и квартира через пробел", 14, 1, "W", 14, 70)
        self.house_appt = self.draw_entry("white", "left", 14, 0, 14, 150)
        self.draw_button("Договор", self.entry_text, 15, 0, 15, 50)
        self.draw_button("Добавить номер в базу", self.add_to_db, 18, 0, 18, 50)
        self.draw_button("Обновить данные", self.refresh, 0, 3, 0, 50)
        self.root.mainloop()


if __name__ == "__main__":
    first = Window(750, 750, "Зарегистрировать абонента Крымтелеком")
    first.run()
