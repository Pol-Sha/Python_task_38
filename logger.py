from data_create import name_data, surname_data, phone_data, address_data
import sys

sys.path.append("/path/to/pandas")


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(
        input(
            f"В каком формате записать данные? \n\n"
            f"1 Вариант: \n"
            f"{name}\n{surname}\n{phone}\n{address}\n\n"
            f"2 Вариант: \n"
            f"{name};{surname};{phone};{address}\n\n"
            f"Выберите вариант: "
        )
    )
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("Введите цифру 1 или 2: "))

    if var == 1:
        with open("data_first_variant.csv", "a", encoding="utf -8") as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open("data_second_variant.csv", "a", encoding="utf -8") as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")


def print_data():
    print("Вывожу данные из 1 файла: ")
    with open("data_first_variant.csv", "r", encoding="utf -8") as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first == "\n\n" or i == len(data_first) - 1:
                data_first_list.append("".join(data_first[j : i + 1]))
                j = i
        print("".join(data_first_list))

    print("Вывожу данные из 2 файла: ")
    with open("data_second_variant.csv", "r", encoding="utf -8") as f:
        data_second = f.readlines()
        print(data_second)


def change_data():
    var = int(
        input(
            f"В каком файле изменить данные? 1 файл или 2 файл? \n\n"
            f"Выберите вариант: "
        )
    )
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("Введите цифру 1 или 2: "))
    if var == 1:
        with open("data_first_variant.csv", "r", encoding="utf-8") as f:
            data = f.readlines()
            print("Выберите из списка ниже, данные которые хотите изменить: ")
            print(*data)
        number_str = int(input("Введите номер строки, которую хотите изменить: "))
        while number_str < 1 or number_str > len(data):
            print("Неправильный номер строки")
            number_str = int(input("Введите номер строки, которую хотите изменить: "))
        new_data = input("Введите новые данные: ")

        data[number_str - 1] = new_data + " \n"

        with open("data_first_variant.csv", "w", encoding="utf-8") as f:
            f.writelines(data)
        print("Спасибо, изменения сохранены")
    elif var == 2:
        with open("data_second_variant.csv", "r", encoding="utf-8") as f:
            data = f.readlines()

        print("Доступные данные для изменения:")
        print(*data)

        number_str = int(input("Введите номер строки, которую хотите изменить: "))
        while number_str < 1 or number_str > len(data):
            print("Неправильный номер строки")
            number_str = int(input("Введите номер строки, которую хотите изменить: "))

        new_data = (
            name_data()
            + "; "
            + surname_data()
            + "; "
            + phone_data()
            + "; "
            + address_data()
        )

        data[number_str - 1] = new_data + "\n"

        with open("data_second_variant.csv", "w", encoding="utf-8") as f:
            f.writelines(data)
        print("Спасибо, изменения сохранены")


def delete_data():
    var = int(
        input(
            f"Из какого файла удалить данные?\n 1 - файл № 1 \n 2 - файл № 2\n"
            f"Введите цифру: "
        )
    )
    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("Введите цифру 1 или 2: "))

    if var == 1:
        with open("data_first_variant.csv", "r", encoding="utf-8") as f:
            data = f.readlines()

        print("Доступные данные для удаления:")
        print(*data)

        number_str = int(input("Введите номер строки, которую хотите удалить: "))
        while number_str < 1 or number_str > len(data):
            print("Неправильный номер строки")
            number_str = int(input("Введите номер строки, которую хотите удалить: "))

        del data[number_str - 1]

        with open("data_first_variant.csv", "w", encoding="utf-8") as f:
            f.writelines(data)
        print("Данные удалены")

    elif var == 2:
        with open("data_second_variant.csv", "r", encoding="utf-8") as f:
            data = f.readlines()

        print("Доступные данные для удаления:")
        print(*data)

        number_str = int(input("Введите номер строки, которую хотите удалить: "))
        while number_str < 1 or number_str > len(data):
            print("Неправильный номер строки")
            number_str = int(input("Введите номер строки, которую хотите удалить: "))

        del data[number_str - 1]

        with open("data_second_variant.csv", "w", encoding="utf-8") as f:
            f.writelines(data)
        print("Данные удалены")


# input_data()

# print_data()
# change_data()
# delete_data()
