# Задача : разработать программу для вычисления
# суммарного годового дохода с налогов.

# Developers : A.Mazenkov  -
#              K.Kravtsov  -
#              A.Mikhailov -

a = input()         # Тип субъекта
b = float(input())  # Доход субьекта

def tax1():        # Для одного субъекта


def tax2(a,b):              # Для супружеской пары

# Заведем Переменные для дохода, начиная с которого, идет переход
# На следующую ступень ставки налогообложения

rate_1 = 18150
rate_2 = 73800 - 18150
rate_3 = 148850 - 73800
rate_4 = 226850 - 148850
rate_5 = 405100 - 226850
rate_6 = 457600 - 405100

# Заведем переменные для налоговых сборов с каждой ступени налога

lim_1 = 0.1 * rate_1
lim_2 = 0.15 * rate_2
lim_3 = 0.25 * rate_3
lim_4 = 0.28 * rate_4
lim_5 = 0.33 * rate_5
lim_6 = 0.35 * rate_6
if b <= 457600:
    if b <= 405100:
        if b <= 226850:
            if b <= 148850:
                if b <= 73800:
                    if b <= 18150:
                        price = 0.1 * b
                    else:
                        price = lim_1 + 0.15 * (b - rate_1)
                else:
                    price = lim_1 + lim_2 + 0.25 * (b - rate_2)
            else:
                price = lim_1 + lim_2 + lim_3 + 0.28 * (b - rate_3)
        else:
            price = lim_1 + lim_2 + lim_3 + lim_4 + 0.33 * (b - rate_4)
    else:
        price = lim_1 + lim_2 + lim_3 + lim_4 + lim_5 + 0.35 * (b - rate_5)
else:
    price = lim_1 + lim_2 + lim_3 + lim_4 + lim_5 + lim_6 + 0.396 * (b - rate_6)


def tax3():         # Для родителя-одиночки


def main():