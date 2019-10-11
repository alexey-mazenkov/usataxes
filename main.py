# Задача : разработать программу для вычисления
# суммарного годового дохода с налогов.

# Developers : A.Mazenkov  -
#              K.Kravtsov  -
#              A.Mikhailov -

subject_type = input()         # Тип субъекта
income = float(input())  # Доход субьекта

def formula(
        first,
        second,
        third,
        fourth,
        fifth,
        sixth
):
    '''
    :param first:
    :param second:
    :param third:
    :param fourth:
    :param fifth:
    :param sixth:
    :return:
    '''

    # Заведем Переменные для дохода, начиная с которого, идет переход
    # На следующую ступень ставки налогообложения

    rate_1 = first
    rate_2 = second
    rate_3 = third
    rate_4 = fourth
    rate_5 = fifth
    rate_6 = sixth

    # Заведем переменные для налоговых сборов с каждой ступени налога

    lim_1 = 0.1 * rate_1
    lim_2 = 0.15 * rate_2
    lim_3 = 0.25 * rate_3
    lim_4 = 0.28 * rate_4
    lim_5 = 0.33 * rate_5
    lim_6 = 0.35 * rate_6
    if income <= 457600:
        if income <= 405100:
            if income <= 226850:
                if income <= 148850:
                    if income <= 73800:
                        if income <= 18150:
                            price = 0.1 * income
                        else:
                            price = lim_1 + 0.15 * (income - rate_1)
                    else:
                        price = lim_1 + lim_2 + 0.25 * (income - rate_2)
                else:
                    price = lim_1 + lim_2 + lim_3 + 0.28 * (income - rate_3)
            else:
                price = lim_1 + lim_2 + lim_3 + lim_4 + 0.33 * (income - rate_4)
        else:
            price = lim_1 + lim_2 + lim_3 + lim_4 + lim_5 + 0.35 * (income - rate_5)
    else:
        price = lim_1 + lim_2 + lim_3 + lim_4 + lim_5 + lim_6 + 0.396 * (income - rate_6)

if subject_type == 'one subject':
    formula()   # Для одного субъекта

if subject_type == 'married couple':
    formula(18150, 55650, 73050, 78000, 178250, 52500) # Для супружеской пары

if subject_type == 'single parent':
formula()   # Для родителя-одиночки


def main():