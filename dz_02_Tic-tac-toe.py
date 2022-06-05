"""Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её, причем чтобы сыграть в нее можно было в
одиночку. """
from random import randint, choice

"Выбираем уровень сложности"
smart_level = 2  # Всего 3 уровня сложности: 0, 1, 2

table = [[None for i in range(3)] for j in range(3)]
empty_cells = ['11', '12', '13', '21', '22', '23', '31', '32', '33']
user_symb = 1  # у игрока крестики
comp_symb = 0  # у компьютера нолики


def print_table():
    for r, row in enumerate(table):
        for c, col in enumerate(row):
            cell = table[r][c]
            cell_char = '   ' if cell is None else ' X ' if cell else ' 0 '
            end_char = '|' if c < 2 else '\n'
            print(cell_char, end=end_char)
        if r < 2:
            print('---+---+---')

def comp_thinking():
    check_symb_list = [comp_symb, user_symb]
    if smart_level:
        for check_symb in check_symb_list[-smart_level:]:
            for cell in empty_cells:
                x, y = map(int, cell)
                table[x - 1][y - 1] = check_symb
                if check_table() == check_symb:
                    table[x - 1][y - 1] = None
                    return cell
                table[x - 1][y - 1] = None
    return choice(empty_cells)

def step(is_player, symb):
    if is_player:
        coord_xy = '-'
        while coord_xy not in empty_cells:
            print('Возможные ходы', empty_cells)
            print('Для завершения нажмите Enter')
            coord_xy = input("Ваш ход (строка столбец без пробела): ")
            if coord_xy == '':
                exit()
    else:
        coord_xy = comp_thinking()
    empty_cells.remove(coord_xy)
    x, y = map(int, coord_xy)
    table[x - 1][y - 1] = symb
    if not is_player:
        print(f'Ход компьютера ({x}, {y})')


def check_table():
    "Проверка есть ли выигрыш"
    # проходим по строкам
    for i in table:
        if i[0] is not None and i[0] == i[1] == i[2]:
            return i[0]
    # проходим по столбцам
    for j in range(3):
        col = [i[j] for i in table]
        if col[0] is not None and col[0] == col[1] == col[2]:
            return col[0]
    # проверяем диагонали
    if table[0][0] is not None and table[0][0] == table[1][1] == table[2][2]:
        return table[0][0]
    if table[2][0] is not None and table[2][0] == table[1][1] == table[0][2]:
        return table[2][0]
    # проверяем заполнена ли таблица
    for item in table:
        if list(filter(lambda i: i is None, item)) != []:
            break
    else:
        return 'ничья'
    return None


def play_game():
    check = None
    turn_X = True  # показывает чей ход
    # Основной цикл игры
    # Игра идет пока функция chek не вернет результат отличный от None
    while check is None:
        step(turn_X, user_symb if turn_X else comp_symb)
        if not turn_X:
            print_table()
        check = check_table()
        turn_X = not turn_X
    if check is not None:
        if check == user_symb:
            print_table()
            print("Поздравляю, вы победили!!")
        elif check == comp_symb:
            print("Победил компьютер")
        else:
            print("Ничья!")


if __name__ == '__main__':
    play_game()
