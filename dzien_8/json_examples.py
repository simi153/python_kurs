import json

lista = [1,2,3]
slownik={
    "ala":"kot",
    "lista":lista
}
with open("dane/dane2.json","w") as f:
    json.dump(slownik,f)
#(print(json.dumps(slownik))

with open("dane/dane.json") as f:
    dane=json.load(f)

