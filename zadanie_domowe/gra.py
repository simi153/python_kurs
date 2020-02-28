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
    def __init__(self, name, *typ):
        self.name = name
        self.w_ekwipunku = False
        if typ:
            if typ[0] == "off":
                self.do_sily = fake.random.randint(1, 20)
                self.do_obrony = 0
                self.do_zrecznosci = 0
            elif typ[0] == "deff":
                self.do_obrony = fake.random.randint(1, 20)
                self.do_sily = 0
                self.do_zrecznosci = 0
            elif typ[0] == "dex":
                self.do_zrecznosci = fake.random.randint(1, 20)
                self.do_sily = 0
                self.do_obrony = 0
            else:
                self.do_sily = fake.random.randint(1, 20)
                self.do_obrony = fake.random.randint(1, 20)
                self.do_zrecznosci = fake.random.randint(1, 20)
        else:
            self.do_sily = fake.random.randint(1, 20)
            self.do_obrony = fake.random.randint(1, 20)
            self.do_zrecznosci = fake.random.randint(1, 20)
        self.polozenie = Polozenie.random()

    def __str__(self):
        return f"<{self.name} | STR: {self.do_sily} DEX: +{self.do_zrecznosci} DEF: +{self.do_obrony}>"


class Roslina:
    def __init__(self, name, typ):
        self.name = name
        self.zjedzone = False
        if typ == "lecz":
            self.do_zdrowia = fake.random.randint(1, 10)
        if typ == "truj":
            self.do_zdrowia = fake.random.randint(-10, 0)
        self.polozenie = Polozenie.random()

    def __str__(self):
        if self.do_zdrowia > 0:
            return f"<{self.name} | HP: (+{self.do_zdrowia} HP)>"
        else:
            return f"<{self.name} | HP: ({self.do_zdrowia} HP)>"


class Polozenie:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def w(self):
        if self.y < 10:
            self.y += 1
        else:
            print("Nie mozesz wyjść poza planszę!")

    def s(self):
        if self.y > 0:
            self.y -= 1
        else:
            print("Nie mozesz wyjść poza planszę!")

    def a(self):
        if self.x > 0:
            self.x -= 1
        else:
            print("Nie mozesz wyjść poza planszę!")

    def d(self):
        if self.x < 10:
            self.x += 1
        else:
            print("Nie mozesz wyjść poza planszę!")

    @classmethod
    def random(cls):
        return cls(fake.random.randint(1, 10), fake.random.randint(1, 10))


class Postac:
    def __init__(self, name):
        self.name = name
        self.zycie = 100
        self.sila = fake.random.randint(1, 101)
        self.zwinnosc = fake.random.randint(1, 101)
        self.obrona = fake.random.randint(1, 101)
        self.polozenie = Polozenie.random()
        self.ekwipunek = []
        self.rosliny = []

    @classmethod
    def with_fake_name(cls):
        return cls(fake.name())

    def __str__(self):
        return f"<{self.name} \t| HP: {self.zycie}, STR: {self.sila}, DEX: {self.zwinnosc}, DEF: {self.obrona}>"

    @property
    def zyje(self):
        return True if self.zycie > 0 else False

    def otrzymaj_obrazenia(self, moc_ciosu):

        if moc_ciosu > round((self.obrona * (1 + (self.zwinnosc / 100)))):
            print(f"\t{self.name} otrzymuje {moc_ciosu - round((self.obrona * (1 + (self.zwinnosc / 100))))} ",
                  end=" ")
            self.zycie -= moc_ciosu - round((self.obrona * (1 + (self.zwinnosc / 100))))
        else:
            print(f"\t{self.name} otrzymuje 0 obrażeń", end=" ")
        if self.obrona - moc_ciosu >= 0:
            self.obrona -= moc_ciosu
        else:
            self.obrona = 0
        print(f"- (HP: {self.zycie})")

    def zadaj_obrazenia(self):
        base = fake.random.randint(1, self.sila)
        for p in self.ekwipunek:
            base += p.do_sily
        print(f"\t{self.name} zadaje {base} obrażeń")
        return base

    def wez_przedmiot(self, przedmiot):
        if not przedmiot.w_ekwipunku:
            print(f"Znalazłem {przedmiot}")
            self.ekwipunek.append(przedmiot)

    def zjedz_rosline(self, roslina):
        if not roslina.zjedzone:
            print(f"Znalazłem {roslina}")
            self.zycie += roslina.do_zdrowia

    def uzyj_przedmiotow(self):
        for el in self.ekwipunek:
            self.sila += el.do_sily
            self.zwinnosc += el.do_zrecznosci
            self.obrona += el.do_obrony

    @staticmethod
    def walka(postac, postac2):
        while postac.zyje and postac2.zyje:
            print(f"\n\tUderza: {postac2.name}")
            postac.otrzymaj_obrazenia(postac2.zadaj_obrazenia())
            print(f"\n\tUderza: {postac.name}")
            postac2.otrzymaj_obrazenia(postac.zadaj_obrazenia())
        if not postac.zyje:
            print("Game Over")
            return False
        return True


postac = Postac("Zenek")
postac2 = Postac.with_fake_name()
siekiera = Przedmiot("Krwawa siekiera!")
buty = Przedmiot("Buty Usain Bolta!", "dex")
tarcza = Przedmiot("Drewniana tarcza!", "deff")
jagody = Roslina("Jadalne jagody", "lecz")
grzyby = Roslina("Trujace grzyby!", "truj")
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

    print(postac.name, postac.polozenie, end="  ")
    if DEBUG:
        print(postac)
        print(postac2.name, postac2.polozenie)
        print(siekiera.name, siekiera.polozenie)
        print(buty.name, buty.polozenie)
        print(tarcza.name, tarcza.polozenie)
        print(jagody.name, jagody.polozenie)
        print(grzyby.name, grzyby.polozenie)

    if postac.polozenie == postac2.polozenie:
        postac.uzyj_przedmiotow()
        print("\n\nKonfrontacja!!!")
        print(postac)
        print(postac2)
        wynik = Postac.walka(postac, postac2)
        if wynik is False:
            break
    if postac.polozenie == siekiera.polozenie:
        postac.wez_przedmiot(siekiera)
        siekiera.w_ekwipunku = True
    if postac.polozenie == buty.polozenie:
        postac.wez_przedmiot(buty)
        buty.w_ekwipunku = True
    if postac.polozenie == tarcza.polozenie:
        postac.wez_przedmiot(tarcza)
        tarcza.w_ekwipunku = True
    if postac.polozenie == jagody.polozenie:
        postac.zjedz_rosline(jagody)
        print(postac)
        jagody.zjedzone = True
    if postac.polozenie == grzyby.polozenie:
        postac.zjedz_rosline(grzyby)
        print(postac)
        grzyby.zjedzone = True
