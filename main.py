# Задача : разработать программу для вычисления
# суммарного годового дохода с налогов.

# Developers : A.Mazenkov  -
#              K.Kravtsov  -
#              A.Mikhailov -

def formula(
        income,
        first,
        second,
        third,
        fourth,
        fifth,
        sixth
):
    """

    :param income:
    :param first:
    :param second:
    :param third:
    :param fourth:
    :param fifth:
    :param sixth:
    :return:
    """

    # Заведем Переменные для дохода, начиная с которого, идет переход
    # На следующую ступень ставки налогообложения

    rate_1 = first
    rate_2 = second - first
    rate_3 = third - second
    rate_4 = fourth - third
    rate_5 = fifth - fourth
    rate_6 = sixth - fifth

    # Заведем переменные для налоговых сборов с каждой ступени налога

    lim_1 = 0.1 * rate_1
    lim_2 = 0.15 * rate_2
    lim_3 = 0.25 * rate_3
    lim_4 = 0.28 * rate_4
    lim_5 = 0.33 * rate_5
    lim_6 = 0.35 * rate_6
    if income <= sixth:
        if income <= fifth:
            if income <= fourth:
                if income <= third:
                    if income <= second:
                        if income <= first:
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



def main():
    subject_type = input()  # Тип субъекта
    number_month = int(input())
    name_month = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    i = 0
    price = 0
    all_price = 0
    income = 0
    while i < number_month:
        income_month = float(input())  # Доход субьекта за месяц
        print('Income for', name_month[i], 'made up', income_month)
        income += income_month
        i += 1
    print('Income for year made up', income)
    if subject_type == 'one subject':
        formula(income, 9075, 36900, 89350, 186350, 405100, 406750)  # Для одного субъекта

    elif subject_type == 'married couple':
        formula(income, 18150, 73800, 148850, 226850, 405100, 457600)  # Для супружеской пары

    elif subject_type == 'single parent':
        formula(income, 12950, 49400, 127550, 206600, 405100, 432200)  # Для родителя-одиночки
    else:
        print('Введите верное имя субъекта')
    all_price += price
    print('Аnnual tax deductions are equal', all_price)

main()