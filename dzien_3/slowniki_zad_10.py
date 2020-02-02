napis = input("Podaj jakis napis: ")
litery = {}
for litera in napis:
    # if litery.get(litera.lower()) == None:
    #     litery[litera.lower()] = 1
    # else:
    #     litery[litera.lower()] += 1
    litery[litera] = litery.get(litera, 0) + 1

    # from collections import defaultdict
    #
    # zliczenia=defaultdict(int)
    # for litera in napis.lower():
    #   litery[litera] += 1

for k, v in litery.items():
    print(f"{k} - {v}")
