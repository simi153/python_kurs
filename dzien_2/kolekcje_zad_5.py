print("    ", end="")
for i in range(10):
    print(f"{i:2}", end=" ")
print()
print()
for i in range(10):
    print(i, end="  ")
    for j in range(10):
        wynik = i * j
        print(f" {wynik:2}", end="")
    print()
