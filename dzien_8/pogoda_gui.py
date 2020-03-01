import tkinter

from pogoda import get_location_id,get_location_weather
def get_weather():
    city = city_entry.get()
    location_id = get_location_id(city)
    weather = get_location_weather(location_id)
    wynik.configure(text=weather.raport())

root = tkinter.Tk()
city_entry = tkinter.Entry(root)
submit = tkinter.Button(root, text="Pobierz pogode", command=get_weather)
wynik=tkinter.Label(root, text="")
city_entry.grid(row=1,column=1)
submit.grid(row=2,column=1)
wynik.grid(row=1,column=3)
root.mainloop()
