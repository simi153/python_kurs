import sys
import csv
from collections import defaultdict

if len(sys.argv) > 1:
    plik = sys.argv[1]
else:
    plik = "dane/Baza_teleadresowa.csv"

with open(plik) as baza:
    reader = csv.DictReader(baza, delimiter=";")
    dane=[]
    for row in reader:
        dane.append((row['Kod_TERYT'],row['telefon kierunkowy']+ row['telefon'].replace(" ","").replace("\n","")))

with open("dane/dane_out.csv","w", newline="") as out:
    writer = csv.writer(out,delimiter=";")
    writer.writerow(["TERYT","TELEFON"])
    writer.writerows(dane)