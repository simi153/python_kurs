class Osoba:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"<Osoba {self.name}>"


os1 = Osoba("Bartek")
print(os1)

os2 = Osoba("Ania")
print(os2)
