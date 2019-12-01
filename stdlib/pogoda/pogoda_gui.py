import tkinter

from pogoda import wypisz_id, get_location_weather, prepare_weather_report

def get_weather():
    location_name = location_entry.get()
    location_id = wypisz_id(location_name)
    weather = get_location_weather(location_id)
    report = prepare_weather_report(weather, location_name)
    result_label.configure(text=report)

root = tkinter.Tk()


location_entry = tkinter.Entry(master=root)
result_label = tkinter.Label(master=root, text="")
get_button = tkinter.Button(master=root, text="Pobierz", command=get_weather)

location_entry.pack()
result_label.pack()
get_button.pack()

root.mainloop()