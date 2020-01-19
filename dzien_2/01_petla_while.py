i = 1
temperatura = 0
while i <= 7:
    temperatura += float(input(f"Podaj temperature dnia {i}: "))
    i = i + 1

srednia = temperatura / (i - 1)
print(f"Srednia temperatura z {i - 1} dni wynosi: {srednia:.0f} st.")
