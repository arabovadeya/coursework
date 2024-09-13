import tkinter as tk
from tkinter import *
from tkinter import ttk


m_gender_list = ["м", "мужской", "муж", "М"]
w_gender_list = ["ж", "женский", "жен", "Ж"]

titles_data_list = ["янв", "фев", "мар", "апр", "май", "мая", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]
numbers_data_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

obl_list = ["Амурской", "Архангельской", "Астраханской", "Белгородской", "Брянской", "Владимирской", "Волгоградской",
            "Вологодской", "Воронежской", "Ивановской", "Иркутской", "Калининградской", "Калужской", "Кемеровской",
            "Кировской", "Костромской", "Курганской", "Курской", "Ленинградской", "Липецкой", "Магаданской",
            "Московской", "Мурманской", "Нижегородской", "Новгородской", "Новосибирской", "Омской", "Оренбургской",
            "Орловской", "Пензенской", "Псковской", "Ростовской", "Рязанской", "Самарской", "Саратовской",
            "Сахалинской", "Свердловской", "Смоленской", "Тамбовской", "Тверской", "Томской", "Тульской", "Тюменской",
            "Ульяновской", "Челябинской", "Ярославской", "Еврейской"]

kr_list = ["Алтайского", "Забайкальского", "Камчатского", "Краснодарского", "Красноярского", "Пермского", "Приморского",
           "Ставропольского", "Хабаровского"]

ao_list = ["Ненецкий", "Ханты-Мансийский", "Чукотский", "Ямало-Ненецкий"]


def entry_input_error(entry):
    entry.delete(0, END)
    entry.insert(0, "Некорректный ввод!")


def text_input_error(text):
    text.delete("1.0", END)
    text.insert("1.0", "Некорректный ввод!")


def correct_data(lst, entry):  # Исправление даты
    flag = 0
    # День
    if len(lst[0]) == 1:
        lst[0] = "0" + lst[0]
    elif len(lst[0]) > 2 or int(lst[0]) > 31:
        flag = 1

    # Месяц
    if lst[1][:3] in titles_data_list:
        for i in range(len(titles_data_list)):
            if lst[1][:3] == titles_data_list[i]:
                lst[1] = numbers_data_list[i]
                break
    elif len(lst[1]) == 1 or len(lst[1]) == 2:
        if len(lst[1]) == 1:
            lst[1] = "0" + lst[1]

        if lst[1] not in numbers_data_list:
            flag = 1

    # Год
    if len(lst[2]) == 1:
        lst[2] = "0" + lst[2]

    if len(lst[2]) == 2:
        if int(lst[2]) > 22:
            lst[2] = "19" + lst[2]
        else:
            lst[2] = "20" + lst[2]
    elif len(lst[2]) == 4:
        if lst[2][:1] != "1" and lst[2][:1] != "2":
            flag = 1
    else:
        flag = 1

    if flag:
        entry_input_error(entry)
    else:
        entry.delete(0, END)
        entry.insert(0, lst[0] + "." + lst[1] + "." + lst[2])


def date(entry):  # Дата рождения и выдачи
    if entry.get().find(".") != -1:
        lst = entry.get().split(".")
        if len(lst) != 3:
            entry_input_error(entry)
        else:
            correct_data(lst, entry)
    elif entry.get().isdigit():
        if len(entry.get()) == 8:
            lst = entry.get()[:2] + "." + entry.get()[2:4] \
                  + "." + entry.get()[4:8]
            correct_data(lst.split("."), entry)

        elif len(entry.get()) == 6:
            lst = entry.get()[:2] + "." + entry.get()[2:4] \
                  + "." + entry.get()[4:6]
            correct_data(lst.split("."), entry)

        elif len(entry.get()) == 5:
            lst = entry.get()[:1] + "." + entry.get()[1:3] \
                  + "." + entry.get()[3:5]
            correct_data(lst.split("."), entry)
        elif len(entry.get()) == 4:
            lst = entry.get()[:1] + "." + entry.get()[1:2] \
                  + "." + entry.get()[2:4]
            correct_data(lst.split("."), entry)
        else:
            entry_input_error(entry)
    else:
        entry_input_error(entry)


def division_code():  # Код подразделения
    if entry_division_code.get().isdigit():
        if len(entry_division_code.get()) != 6:
            entry_input_error(entry_division_code)
        else:
            entry_division_code.insert(0, entry_division_code.get()[:3] + "-" + entry_division_code.get()[3:])
            entry_division_code.delete(7, END)

    elif len(entry_division_code.get()) == 7:
        if entry_division_code.get()[0:3].isdigit() and entry_division_code.get()[3:4] == "-" \
                and entry_division_code.get()[0:3].isdigit():
            pass
        else:
            entry_input_error(entry_division_code)
    else:
        entry_input_error(entry_division_code)


def series_and_number():  # Серия и номер
    if entry_series.get().isdigit():
        if len(entry_series.get()) == 4:
            entry_series.insert(0, entry_series.get()[:2] + " " + entry_series.get()[2:])
            entry_series.delete(5, END)
        else:
            entry_input_error(entry_series)

    elif len(entry_series.get()) == 5:
        if entry_series.get()[0:2].isdigit() and entry_series.get()[2:3] == " " \
                and entry_series.get()[3:5].isdigit():
            pass
        else:
            entry_input_error(entry_series)
    else:
        entry_input_error(entry_series)

    if entry_number.get().isdigit():
        if len(entry_number.get()) != 6:
            entry_input_error(entry_number)
    else:
        entry_input_error(entry_number)


def gender():  # Пол
    if [i for i in m_gender_list if i == entry_gender.get()]:
        entry_gender.delete(0, END)
        entry_gender.insert(0, "муж.")
    elif [i for i in w_gender_list if i == entry_gender.get()]:
        entry_gender.delete(0, END)
        entry_gender.insert(0, "жен.")
    else:
        entry_input_error(entry_gender)


def fio():  # Имя
    if not entry_fio.get().isdigit():
        tmp = entry_fio.get().title()
        entry_fio.delete(0, END)
        entry_fio.insert(0, tmp)
    else:
        entry_input_error(entry_fio)


def place_birth():
    lst = text_place_birth.get("1.0", END).split(" ")

    if len(lst) > 5 or len(lst) < 4:
        text_input_error(text_place_birth)
    else:
        if lst[0][:1] == "г" or lst[0][:1] == "Г":
            lst[0] = "гор."
        elif lst[0][:1] == "с" or lst[0][:1] == "С":
            lst[0] = "сел."
        elif lst[0][:1] == "п" or lst[0][:1] == "П":
            lst[0] = "пос."
        elif lst[0][:1] == "д" or lst[0][:1] == "Д":
            lst[0] = "дер."
        else:
            lst[0] = "Некорректный ввод!"

        if lst[1][:1].islower():
            lst[1] = lst[1].title()
        if lst[2][:1].islower():
            lst[2] = lst[2].title()

        flag = 0
        if lst[3][:1] == "о" or lst[3][:1] == "О":
            lst[3] = "обл."
            for i in obl_list:
                if i.find(lst[2][:4]) != -1:
                    lst[2] = i
                    flag = 1
                    break

        elif lst[3][:1] == "к" or lst[3][:1] == "К":
            lst[3] = "края"
            for i in kr_list:
                if i.find(lst[2][:5]) != -1:
                    lst[2] = i
                    flag = 1
                    break

        elif lst[3][:1] == "а" or lst[3][:1] == "А":
            lst[3] = "AO"
            for i in ao_list:
                if i.find(lst[2][:3]) != -1:
                    lst[2] = i
                    flag = 1
                    break
        else:
            lst[3] = "Некорректный ввод!"

        if flag == 0:
            lst[2] = "Некорректный ввод!"

        text_place_birth.delete("1.0", END)
        text_place_birth.insert("1.0", lst[0] + lst[1] + "\n" + lst[2] + " " + lst[3] + "\n" + "Россия")


def issued_by():
    lst = text_issued_by.get("1.0", END).split(" ")

    flag = 0
    if lst[len(lst) - 1][:2] == "об" or lst[len(lst) - 1][:2] == "Об" or lst[len(lst) - 1][:2] == "ОБ":
        lst[len(lst) - 1] = "области"
        lst[len(lst) - 2] = lst[len(lst) - 2].title()
        for i in obl_list:
            if i.find(lst[len(lst)-2][:4]) != -1:
                lst[len(lst) - 2] = i
                flag = 1
                break

    elif lst[len(lst) - 1][:1] == "к" or lst[len(lst) - 1][:1] == "К":
        lst[len(lst) - 1] = "краю"
        lst[len(lst) - 2] = lst[len(lst) - 2].title()
        for i in kr_list:
            if i.find(lst[len(lst)-2][:4]) != -1:
                lst[len(lst) - 2] = i.replace("ого", "ому")
                flag = 1
                break
    else:
        for i in range(len(lst)):
            if lst[i].find("окр") != -1 or lst[i].find("Окр") != -1 or lst[i].find("ОКР") != -1:
                lst[i] = "округа"
                flag = 1
            if lst[i].find("гор") != -1 or lst[i].find("Гор") != -1 or lst[i].find("ГОР") != -1:
                lst[i] = "города"
                flag = 1
                
            if lst[i].find("сел") != -1 or lst[i].find("Сел") != -1 or lst[i].find("СЕЛ") != -1:
                lst[i] = "селе"
                flag = 1
                
            if lst[i].find("пос") != -1 or lst[i].find("Пос") != -1 or lst[i].find("ПОС") != -1:
                lst[i] = "поселке"
                flag = 1
                
            if lst[i].find("дер") != -1 or lst[i].find("Дер") != -1 or lst[i].find("ДЕР") != -1:
                lst[i] = "деревне"
                flag = 1
            

    if flag == 1:
        text_issued_by.delete("1.0", END)
        text_issued_by.insert("1.0", " ".join(lst))

    else:
        text_input_error(text_issued_by)


def button_event():
    fio()
    date(entry_date_birth)
    gender()
    place_birth()
    issued_by()
    division_code()
    series_and_number()
    date(entry_date_issue)


root = Tk()

root.title('Проверка корректности паспортных данных')
root.geometry('600x400+300+300')
root.resizable(FALSE, FALSE)

ttk.Label(text=" Ф.И.О:").grid(row=0, column=0, sticky=tk.W)
entry_fio = ttk.Entry()
entry_fio.grid(row=0, column=2, columnspan=2, sticky=tk.W + tk.E, pady=5)

ttk.Label(text=" Дата рождения:").grid(row=1, column=0, sticky=tk.W)
entry_date_birth = ttk.Entry()
entry_date_birth.grid(row=1, column=2, columnspan=2, sticky=tk.W + tk.E, pady=5)

ttk.Label(text=" Пол:").grid(row=2, column=0, sticky=tk.W)
entry_gender = ttk.Entry()
entry_gender.grid(row=2, column=2, columnspan=2, sticky=tk.W + tk.E, pady=5)

ttk.Label(text="Место рождения:").grid(row=3, column=0, sticky=tk.W)
text_place_birth = Text(width=20, height=3)
text_place_birth.grid(row=3, column=2, columnspan=2, sticky=tk.W + tk.E, pady=5)

ttk.Label(text="Кем выдан:").grid(row=4, column=0, sticky=tk.W)
text_issued_by = Text(width=20, height=3)
text_issued_by.grid(row=4, column=2, columnspan=2, sticky=tk.W + tk.E, pady=5)

ttk.Label(text="Код подразделения:").grid(row=6, column=0, sticky=tk.W)
entry_division_code = ttk.Entry()
entry_division_code.grid(row=6, column=2, columnspan=2, sticky=tk.W + tk.E, pady=5)

ttk.Label(text=" Cерия и номер:").grid(row=7, column=0, sticky=tk.W)
entry_series = ttk.Entry()
entry_series.grid(row=7, column=2, columnspan=2, sticky=tk.W + tk.E, pady=5)
entry_number = ttk.Entry()
entry_number.grid(row=7, column=4, columnspan=2, sticky=tk.W + tk.E, pady=5)

ttk.Label(text=" Дата выдачи:").grid(row=8, column=0, sticky=tk.W)
entry_date_issue = ttk.Entry()
entry_date_issue.grid(row=8, column=2, columnspan=2, sticky=tk.W + tk.E, pady=5)

btn = ttk.Button(root, text="Проверить", command=button_event, width=10)
btn.grid(row=9, column=0, columnspan=3)

root.mainloop()
