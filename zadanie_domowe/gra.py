"""
Stwórz klasę Postac
która ma atrybuty
- imie
- zycie
- sila
- zwinnosc
- obrona
* Przu uzyciu biblioteki Faker stwórz mechanizm
tworzenia losowych postaci
postaca w czasie tworzenia umiejscowiana jest gdzies na planszy
pip install faker
Klasa Przedmiot
- nazwa
- bonusy: do_sily, do_obrony,
przedmiot ma położenie
przedmiot może byc dodany do ekwipunku
jak sie tam znajduje o powieksza statystyki
"""

from faker import Faker

fake = Faker("pl_PL")

DEBUG = True

# print(fake.name())
# print(fake.text())
# print(fake.random.randint(1, 101))


class Przedmiot:
    def __init__(self, name):
        self.name = name
        self.do_sily = fake.random.randint(1, 20)
        self.do_obrony = fake.random.randint(1, 20)
        self.polozenie = Polozenie.random()

    def __str__(self):
        return f"<{self.name} | s: +{self.do_sily}>"


class Polozenie:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def w(self):
        self.y += 1

    def s(self):
        self.y -= 1

    def a(self):
        self.x -= 1

    def d(self):
        self.x += 1

    @classmethod
    def random(cls):
        return cls(fake.random.randint(1, 10), fake.random.randint(1, 10))


class Postac:
    def __init__(self, name):
        self.name = name
        self.zycie = fake.random.randint(1, 101)
        self.sila = fake.random.randint(1, 101)
        self.zwinnosc = fake.random.randint(1, 101)
        self.obrona = fake.random.randint(1, 101)
        self.polozenie = Polozenie.random()
        self.ekwipunek = []

    @classmethod
    def with_fake_name(cls):
        return cls(fake.name())

    def __str__(self):
        return f"<{self.name} | e: {self.zycie}, s: {self.sila}, a: {self.zwinnosc}, d: {self.obrona}>"

    @property
    def zyje(self):
        return True if self.zycie > 0 else False

    def otrzymaj_obrazenia(self, moc_ciosu):
        print("Otrzymuje obrazenia", moc_ciosu)
        self.zycie -= moc_ciosu

    def zadaj_obrazenia(self):
        base = fake.random.randint(1, self.sila)
        for p in self.ekwipunek:
            base += p.do_sily
        return

    def wez_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)

    @staticmethod
    def walka(postac, postac2):
        while postac.zyje and postac2.zyje:
            print(f"Uderza: {postac2.name}")
            postac.otrzymaj_obrazenia(postac2.zadaj_obrazenia())
            print(f"Uderza: {postac.name}")
            postac2.otrzymaj_obrazenia(postac.zadaj_obrazenia())
        if not postac.zyje:
            print("Game Over")
            return False
        return True


postac = Postac("Zenek")
postac2 = Postac.with_fake_name()
siekiera = Przedmiot("Krwawa siekiera!")
#
# while postac.zyje and postac2.zyje:
#     print(f"Uderza: {postac2.name}")
#     postac.otrzymaj_obrazenia(postac2.zadaj_obrazenia())
#     print(f"Uderza: {postac.name}")
#     postac2.otrzymaj_obrazenia(postac.zadaj_obrazenia())
#
# print(f"{postac.name} {postac.zyje}")
# print(f"{postac2.name} {postac2.zyje}")

# poruszanie sie

while True:
    kierunek = input("W która strone w (góra) s (dół) a(lewo) d(prawo)")
    # ruch = getattr(postac.polozenie, kierunek)
    # ruch()

    try:
        getattr(postac.polozenie, kierunek)()
    except AttributeError:
        print("Nie znam takiego kierunku")

    print(postac.name, postac.polozenie)
    print(postac2.name, postac2.polozenie)
    print(siekiera.name, siekiera.polozenie)

    if postac.polozenie == postac2.polozenie:
        print("Konfrontacja!!!")
        wynik = Postac.walka(postac, postac2)
        if wynik is False:
            break
    if postac.polozenie == siekiera.polozenie:
        print(f"Znalazłem {siekiera}")