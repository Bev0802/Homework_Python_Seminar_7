import csv

def data_request():
    dr = int(input(
        "\nВведите номер действия, которое вы хотите совершить:\n" 
            "0 - создать контакт.\n"
            "1 - посмотреть телефонную книгу.\n"
            "2 - посмотреть только имя и фамилию.\n"
            "3 - отсортировать по имени.\n"
            "4 - отсортировать по ID.\n"
            "5 - для выхода из программы.\n"))
    return dr

def create_contact():
    id = int(input("Номер по порядку: "))
    name = input("Имя: ")
    last_name = input("Фамилия: ")
    phone_number = int(input("Номер телефона: "))
    comments = input("Kомментрий: ")
    contact = (f"{id}| {name}| {last_name}| {phone_number}| {comments}\n")   
    with open('Telephone_book.txt', 'a') as file:
        file.write(f'{contact}')
        print(f'Контакт записан в файл Telephone_book.txt: {contact}')
   