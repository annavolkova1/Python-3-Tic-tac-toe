# -*- coding: utf-8 -*-
# В качестве поля создаём одномерный список с числами от 1 до 9
board = list(range(1, 10)) # using list() for supporting Python 3


# Функция вывода игрового поля
def draw_board(board):
    print("-------------") # using print() instead of raw_print for supporting Python 3
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-------------")


# Функция обработки пользовательского ввода
def take_input(player_token):
    """Если число не от 1 до 9, а больше или меньше, то выводится это сообщение -
    Некорректный ввод. Введите число от 1 до 9.
    """
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer - 1]) not in "XO"):
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


# Функция проверки игрового поля
def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


# Функция объединяющая другие функции в игру
def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)

def _doctests():
    import doctest
    doctest.testmod()

# Запуск игры
main(board)