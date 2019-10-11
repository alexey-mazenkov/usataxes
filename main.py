# Developers : A.Mazenkov  -
#              K.Kravtsov  - 65%
#              A.Mikhailov - 30%

import localization as lc

lc.lang = str()  # Choose the language.


# Tax calculation formula.

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

    # Creation of variables for income
    # starting from which the transition to the next level of the tax rate.

    rate_1 = first
    rate_2 = second - first
    rate_3 = third - second
    rate_4 = fourth - third
    rate_5 = fifth - fourth
    rate_6 = sixth - fifth

    # Creating Variables for Tax Charges from Each Tax Level.

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
    print('{:.2f}'.format(price))


def main():
    print(lc.start_message)
    subject_type = int(input())  # Subject type input.

    number_month = 12
    name_month = [lc.yan, lc.feb, lc.mar, lc.apr, lc.may, lc.jun, lc.jul, lc.aug, lc.sep, lc.october, lc.nov, lc.dec]

    i = 0
    income = 0
    while i < number_month:
        print(lc.enter_revenue, name_month[i])
        income_month = float(input())  # Subject income per month.
        print(lc.income_for, name_month[i], lc.made_up, income_month)
        income += income_month
        i += 1

    print(lc.income_year, income)

    print(lc.annual_tax)

    if subject_type == 1:
        formula(income, 9075, 36900, 89350, 186350, 405100, 406750)  # Calculation for one subject.

    elif subject_type == 2:
        formula(income, 18150, 73800, 148850, 226850, 405100, 457600)  # Calculation for a married couple.

    elif subject_type == 3:
        formula(income, 12950, 49400, 127550, 206600, 405100, 432200)  # Calculation for a single parent.


main()
