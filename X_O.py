def create():
    while True:
        size = input("Введите размер поля\n")
        if not size.isdigit():
            print("Введите размер поля в числовом виде")
            continue
        if int(size) % 2 == 0 or (int(size) < 3 or int(size) > 99):
            print("Поле должно быть нечетным и не равным 1 и не больше 99")
            continue
        size = int(size)
        field = [["-"] * size for _ in range(0, size)]
        break
    return field


def show_field(fd):
    len_field = len(str(len(fd)))
    s = "="
    for i in range(len(fd)):
        if len_field > len(str(i)):
            s += "=" * len_field + str(i + 1)
        else:
            s += "=" + str(i + 1)
    print(s)
    for i in range(len(fd)):
        if len_field > len(str(i)):
            s = "=" * ((len_field - len(str(i + 1))) + 1)
        else:
            s = "="
        print(str(i + 1) + s + ("=" * len_field).join(fd[i]))


def input_user(field, user):
    while True:
        print("Ход", "===", user, "===")
        xy = input("Введите координаты (Два целых числа)\n")
        if len(xy.split()) != 2:  # Делаем проверки
            print("!!!Введено меньше или больше 2 координат!!!")
            continue
        x, y = xy.split()
        if not (x.isdigit() and y.isdigit()):
            print("!!!Неверный тип координат!!!")
            continue
        x, y = int(x), int(y)
        if not ((0 < x < len(field) + 1) and (0 < y < len(field) + 1)):
            print("!!!Координаты заходят за поле!!!")
            continue
        if field[x - 1][y - 1] != "-":
            print("!!!Место Занято!!!")
            show_field(field)
            print("!!!!!!!!!!!!!!!!!!")
            continue
        break
    return x, y


def win(field, user):
    w1 = 0
    w2 = 0
    for i in range(len(field)):
        w3 = 0
        if field[i] == [user] * len(field):
            print("===Победа", user, "Горизонтали===")
            return True
        if field[i][i] == user:
            w1 += 1
        for j in range(len(field[i])):
            if field[j][i] == user:
                w3 += 1
            if i + j == len(field) - 1 and field[i][j] == user:
                w2 += 1
            if w3 == len(field):
                print("===Победа", user, "Вертикали===")
                return True
    if w1 == len(field):
        print("===Победа", user, "по Диагонали===")
        return True
    if w2 == len(field):
        print("===Победа", user, "по Обратной Диагонали===")
        return True


def check_draw(fd):
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    t = []
    for i in range(len(fd)):
        t.append(fd[i][i])
        if "X" in fd[i] and "O" in fd[i]:
            c3 += 1
        if len(t) == len(fd):
            if "X" in t and "O" in t:
                c1 += 1
    t1 = []
    for i in range(len(fd)):
        t = []
        for j in range(len(fd)):
            if i + j == len(fd) - 1:
                t1.append(fd[i][j])
            t.append(fd[j][i])
        if "X" in t and "O" in t:
            c2 += 1
    if len(t) == len(fd):
        if "X" in t1 and "O" in t1:
            c4 += 1
    if c2 == c3 == len(fd) and c1 == c4 == 1:
        print("===!Ничья!===")
        return True


def play():
    field = create()
    c = 0
    while c < len(field) * len(field):
        if c % 2 == 0:
            user = "X"
        else:
            user = "O"
        show_field(field)
        x, y = input_user(field, user)
        field[x - 1][
            y - 1] = user
        c += 1
        if check_draw(field):
            break
        if win(field, user):
            break
        if c == len(field) * len(field):
            print("===Ничья===")
    show_field(field)
    print(
        "===Конец Игры===")


print("Игра Крестики и Нолики")
print("Прошу прощение за топорный подход")
print("Но времени было мало")
start = 1
while start:
    play()
    start = input("""Наберите что угодно - начать игру
    Нажмите Enter чтобы выйти - выйти"\n""")
