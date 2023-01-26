import view, modul

def start():
    while True:
        dr = view.data_request()
        if dr == 0:
            view.create_contact()
        elif dr == 1:
            modul.show_telethon_book_txt()
            #modul.show_telethon_book_csv()
        elif dr == 2:
            modul.show_names()
        elif dr == 3:
            modul.sort_names()
        elif dr == 4:
            modul.sort_id()
        elif dr == 5:
            break

