from random import randint


def check(ships, poz_x, poz_y, direction):
    all_ships = [1, 2, 3, 4]
    x = poz_x
    y = poz_y
    free = False
    for i in range(ships):
        if direction == 4 and 0 <= poz_y - ships:
            y = poz_y - i
        elif direction == 2 and poz_x + ships <= 9:
            x = poz_x + i
        elif direction == 6 and 9 >= poz_y + ships:
            y = poz_y + i
        elif direction == 8 and poz_x - ships >= 0:
            x = poz_x - i
        else:
            return free

        if play_board[x][y + 1] in all_ships or play_board[x][y - 1] in all_ships or play_board[x - 1][y - 1] in all_ships or \
                play_board[x + 1][y - 1] in all_ships or play_board[x + 1][y] in all_ships or play_board[x - 1][y] in all_ships or \
                play_board[x + 1][y + 1] in all_ships or play_board[x - 1][y + 1] in all_ships or play_board[x][y] in all_ships:
            return False
        else:
            free = True

    return free


def drukuj_plansze(plansza):
    print("    ", end="")
    for i in range(10):
        print(f"{chr(65 + i):2s}", end=" ")
    print()
    for i in range(10):
        print(f"{str(i + 1):2s}", end="  ")
        for j in range(10):
            print(f"{str(plansza[i][j]):2s}", end=" ")
        print()


def los_kierunku():
    direction = 1
    while direction % 2 != 0:
        direction = randint(2, 8)
    return direction


def create_ship(ships):
    success = False
    poz_x = randint(0, 9)
    poz_y = randint(0, 9)

    direction = los_kierunku()
    while not success:
        try:
            if check(ships, poz_x, poz_y, direction):
                for i in range(ships):
                    if direction == 4:
                        play_board[poz_x][poz_y - i] = ships
                        success = True
                    elif direction == 6:
                        play_board[poz_x][poz_y + i] = ships
                        success = True
                    elif direction == 2:
                        play_board[poz_x + i][poz_y] = ships
                        success = True
                    elif direction == 8:
                        play_board[poz_x - i][poz_y] = ships
                        success = True
            else:
                poz_x = randint(0, 9)
                poz_y = randint(0, 9)
        except:
            continue


play_board = [[0] * 11 for i in range(11)]

for i in range(10):
    for j in range(10):
        play_board[i][j] = ""

create_ship(4)
create_ship(3)
create_ship(3)
create_ship(2)
create_ship(2)
create_ship(2)
create_ship(1)
create_ship(1)
create_ship(1)
create_ship(1)

print()
drukuj_plansze(play_board)
