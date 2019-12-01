

"""
napisz program obliczajacy koszt przejazdu na zadanym dystansie

uzytkowik wprowadza w gui: cena 1l paliwa, spalanie na 100 i dystant
"""
import tkinter


def koszt_przejazdu():
    try:
        dystans = float(dystans_entry.get())
        spalanie = float(spalanie_entry.get())
        cena_litra = int(cena_litra_entry.get())
        w = ((dystans/100) * spalanie) * cena_litra
        wynik.configure(text=f"Koszt przejazdu: {w}")
    except ValueError:
        wynik.configure(text=f"Nieporawne dane")

root = tkinter.Tk()
dystans_label = tkinter.Label(master=root, text="Dystans: ")
dystans_label.grid(row=1, column=1)
dystans_entry = tkinter.Entry(master=root)
dystans_entry.grid(row=2, column=2)

spalanie_label = tkinter.Label(master=root, text="Spalanie: ")
spalanie_label.grid(row=2, column=2)
spalanie_entry = tkinter.Entry(master=root)
spalanie_entry.grid(row=3, column=3)

cena_litra_label = tkinter.Label(master=root, text="Cena za litr paliwa: ")
cena_litra_label.grid(row=3, column=3)
cena_litra_entry = tkinter.Entry(master=root)
cena_litra_entry.grid(row=4, column=4)

add_button = tkinter.Button(master=root, text="Oblicz", command=koszt_przejazdu)
add_button.grid(row=5, column=4)

wynik = tkinter.Label(master=root, text=" ")
wynik.grid(row=5, column=4)

root.mainloop()