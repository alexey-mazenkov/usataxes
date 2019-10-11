# File with localization packages on RU and EN languages.

lang = input('''
Выберите язык:
Choose the language(ru/en):
''')

if lang.lower() == 'ru':

    start_message = '''Выберите тип семейного статуса:
    1 - Одиночный субъект
    2 - Супружеская пара
    3 - Родитель-одиночка
    '''

    income_for = 'Доход за'
    made_up = 'составил'
    income_year = 'Доход за год составил'
    annual_tax = 'Ежегодные налоговые вычеты равны'
    wrong_subject = 'Введите верное имя субъекта'
    enter_revenue = 'Введите доход за'

    yan = 'январь'
    feb = 'февраль'
    mar = 'март'
    apr = 'апрель'
    may = 'май'
    jun = 'июнь'
    jul = 'июль'
    aug = 'апрель'
    sep = 'сентябрь'
    october = 'октябрь'
    nov = 'ноябрь'
    dec = 'декабрь'

elif lang.lower() == 'en':

    start_message = '''
    Choose type of marital status:
    1 - Solitary subject
    2 - Marriage couple
    3 - Single parent
    '''

    income_for = 'Income for'
    made_up = 'made up'
    income_year = 'Income for year made up'
    annual_tax = 'Annual tax deductions are equal'
    wrong_subject = 'Enter the correct subject type'
    enter_revenue = 'Enter revenue for'

    yan = 'JAN'
    feb = 'FEB'
    mar = 'MAR'
    apr = 'APR'
    may = 'MAY'
    yun = 'YUN'
    yul = 'YUL'
    aug = 'AUG'
    sep = 'SEP'
    october = 'OCT'
    nov = 'NOV'
    dec = 'DEC'

else:
    print('''
    Извините, данный язык пока что не поддерживается
    Sorry, this language is not yet supported
    ''')