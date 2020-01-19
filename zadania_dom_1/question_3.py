# Question 3: Accept string from the user and display only those characters which are present at an even index

def even_odd(text,instruction):
    for index,character in enumerate(text):
        if instruction == "parzyste" and index % 2 == 0:
            print(character)
        elif instruction == "nieparzyste" and index % 2 ==1:
            print(character)
        elif instruction != "parzyste" and instruction != "nieparzyste":
            print("Nie rozumiem takiego polecenia :(")


text = input("Wprowadz przykladowy tekst:")
instruction = input("ktore znaki chcesz wyesiwetlic (parzyste/nieparzyste): ").lower()

even_odd(text,instruction)