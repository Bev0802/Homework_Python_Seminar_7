import view

def show_telethon_book_txt():
    with open('Telephone_book.txt', 'r') as file:
        for line in file.readlines():
            print(line, end="")


def show_names():
    with open('Telephone_book.txt', 'r') as file:
        for line in file.readlines():
            l_shn = line.split("|")
            print(f'Имя: {l_shn[1]}, Фамилия: {l_shn[2]}')

def sort_names():
    l_srn=[]
    with open('Telephone_book.txt', 'r+') as file:
        for line in file.readlines():
            l_srn.append(line.split("|"))
        l_srn = sorted(l_srn, key = lambda x: x[1])
        file.seek(0)
        for contact in l_srn:
            file.write("|".join(contact))
    print("Отсортировано по имени и фамилии.")
    with open('Telephone_book.txt', 'r') as file:
        for line in file.readlines():
            print(line, end="")

def sort_id():
    l_srid=[]
    with open('Telephone_book.txt', 'r+') as file:
        for line in file.readlines():
             l_srid.append(line.split("|"))
        l_srid = sorted( l_srid, key = lambda x: x[0])
        file.seek(0)
        for id in  l_srid:
            file.write("|".join(id))
    print("Отсортировано по ID.")
    with open('Telephone_book.txt', 'r') as file:
        for line in file.readlines():
            print(line, end="")