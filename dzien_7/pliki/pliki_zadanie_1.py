import sys

if len(sys.argv)>1:
    plik=sys.argv[1]
else:
    plik = "dane/emails.txt"

try:
    with open(plik) as em:
        for i, line in enumerate(em):
            print(f"{i + 1}: ", line[:-1])
except FileNotFoundError:
    print("Brak takiego pliku!")