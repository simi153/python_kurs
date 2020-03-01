import tkinter
import pogoda

def sumuj():
    a = a_entry.get()
    b = b_entry.get()
    suma = int(a) + int(b)
    wynik.configure(text=suma)


root = tkinter.Tk()
label_a = tkinter.Label(root, text="a")
label_a.pack()
a_entry = tkinter.Entry(root)
a_entry.pack()
label_b = tkinter.Label(root, text="b")
label_b.pack()
b_entry = tkinter.Entry(root)
b_entry.pack()
submit = tkinter.Button(root, text="Sumuj", command=sumuj)
submit.pack()
wynik=tkinter.Label(root, text="-")
wynik.pack()

root.mainloop()
