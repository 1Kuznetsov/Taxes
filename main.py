import ru_local as ru

# Kuznetsov Igor , Yadreeva Maria

t_salary = 0
t_tax = 0
stoppage = 0
month = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
         "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

days = int(input(ru.DAYS))
if days >= 183:
    resident = 1
else:
    resident = 0
for num in range(12):
    print(ru.SALARY, f"{month[num]}: ", end='')
    t_salary += float(input())

property_t1 = float(input(ru.PROPERTY_T1))
property_t2 = float(input(ru.PROPERTY_T2))
property_t3 = float(input(ru.PROPERTY_T3))
rent = float(input(ru.RENT))
investing = float(input(ru.INVESTING))
deposits = float(input(ru.DEPOSIT))
max_key_rate = float(input(ru.MAX_KEY_RATE))
prize = float(input(ru.PRIZE))
prize_ad = float(input(ru.PRIZE_AD))
estate = float(input(ru.ESTATE))
other_estate = float(input(ru.OTHER_ESTATE))
foreign_income = float(input(ru.FOREIGN_INCOME))

t_income = t_salary + investing + deposits + prize + prize_ad
t_income += estate + rent

if deposits > 1_000_000 * max_key_rate:
    t_tax += (deposits - 1_000_000 * max_key_rate) * 0.13

if resident:
    if t_income > 5_000_000:
        t_tax += (t_salary + investing) * 0.15
    else:
        t_tax += (t_salary + investing) * 0.13
    t_tax += property_t1 * 0.001 + property_t2 * 0.02 + property_t3 * 0.005
    t_tax += 0.13 * rent
    t_tax += (prize - 4000) * 0.13
    t_tax += (prize_ad - 4000) * 0.35
    special = input(ru.SPECIAL).lower()
    if special == "нет":
        t_tax += (estate + other_estate) * 0.13
    t_tax += foreign_income * 0.13
else:
    question_1 = input('''Вы отсутствовали в стране по причинам прохождения лечения,
    обучения или исполнения за границей обязательств по трудовому договору? ''')
    question_2 = input('''Вы российский военнослужащий, который несет воинскую обязанность за границей
    или сотрудник органов власти в командировке за пределами РФ? ''')
    if question_1.lower() == 'нет' and question_2.lower() == 'нет':
        print("Вы нерезидент, налоговые вычеты не предоставляются")
    if question_1.lower() == 'да' and question_2.lower() == 'да':
        print(f'Вы резидент, Ваш налог составляет {t_income}')
    dividends = input('Получали ли Вы дивиденды от долевого участия в деятельности российских организаций? ')
    if dividends.lower() == 'да':
        n_div = float(input('Какой доход от дивидентов? '))
        tax_dividends = n_div * 0.15
    else:
        tax_dividends = 0
    tax_dep = 0
    if max_key_rate * 10_000 < deposits:
        tax_dep = 0
    else:
        tax_dep += deposits * 0.13
    property_non_resident = property_t1 + property_t2 + property_t3 + estate
    question_3 = input("Работаете ли Вы по патенту? ")
    question_4 = input("Являетесь ли Вы высококвалификационным работником? ")
    question_5 = input('''Являетесь ли Вы гражданином государств-членов ЕАЭС 
    (Беларуси, Казахстана, Киргизии, Армении)? ''')
    question_6 = input('''Вы участник Госпрограммы по оказанию содействия добровольному переселению в РФ
    соотечественников, проживающих за рубежом, а также членов их семей? ''')
    question_7 = input("Вы член экипажа судов, плавающих по Государственным флагом РФ? ")
    question_8 = input("Являетесь ли Вы беженцем или получившим временное убежище в РФ? ")
    if question_3.lower() == 'нет' or question_4.lower() == 'нет' or question_5.lower() == 'нет' or question_6.lower() == 'нет' or question_7.lower() == 'нет' or question_8.lower() == 'нет':
        tax_non_resident_1 = (investing + t_salary + rent + estate + prize_ad + prize) * 0.3
        tax_non_resident_1 += tax_dividends + property_non_resident * 0.2 * 0.01 + tax_dep
        print(f'Ваш налог составляет {tax_non_resident_1}')
    else:
        tax_non_resident = (investing + t_salary + rent + estate + prize_ad + prize) * 0.13
        tax_non_resident += tax_dividends + property_non_resident * 0.2 * 0.01 + tax_dep
        print(f'Ваш налог составляет {tax_non_resident}')

if resident:
    education_child = float(input(ru.EDUCATION_CHILD))
    edu_sibling_own = float(input(ru.EDU_SIBLING_OWN))
    charity = float(input(ru.CHARITY))
    cure = float(input(ru.CURE))
    pension = float(input(ru.PENSION))
    insurance = float(input(ru.INSURANCE))
    phys_cult_health = float(input(ru.PHYS_CULT_HEALTH))
    buy_build = float(input(ru.BUY_BUILD))
    losses = float(input(ru.LOSSES))
    if 0 < education_child <= 50_000:
        if education_child <= t_tax:
            child = education_child * 0.13
        else:
            child = t_tax * 0.13
    else:
        if t_tax >= 50_000:
            child = 50_000 * 0.13
        else:
            child = t_tax * 0.13
    stoppage += child
    if charity >= t_income * 0.25:
        char = charity
    else:
        char = 0.25 * t_income
    social = edu_sibling_own + cure + pension + insurance + phys_cult_health + char
    if social <= 120_000:
        if social <= t_tax:
            stoppage += social * 0.13
        else:
            stoppage += t_tax * 0.13
    else:
        if t_tax >= 120_000:
            stoppage += 120_000 * 0.13
        else:
            stoppage += t_tax * 0.13
    if buy_build > 0:
        received = float(input(ru.RECEIVED))
        if buy_build <= 2_000_000:
            if buy_build * 0.13 <= 260_000 - received:
                stoppage += buy_build * 0.13
            else:
                stoppage += 260_000 - received
        else:
            if received == 0:
                stoppage += 260_000
            else:
                stoppage += 260_000 - received
    if estate != 0 and estate > 1_000_000:
        expenses = float(input(ru.EXPENSES))
        estate_1 = 1_000_000 * 0.13
        estate_2 = expenses * 0.13
        if estate_1 >= estate_2:
            stoppage += estate_1
        else:
            stoppage += estate_2
    else:
        stoppage += estate * 0.13
    if other_estate != 0 and other_estate > 250_000:
        expenses_other = float(input(ru.EXPENSES_OTHER))
        estate_other_1 = 250_000 * 0.13
        estate_other_2 = expenses_other * 0.13
        if estate_other_1 >= estate_other_2:
            stoppage += estate_other_1
        else:
            stoppage += estate_other_2
    else:
        stoppage += other_estate * 0.13
    if losses > investing:
        stoppage += investing * 0.13
    else:
        stoppage += losses * 0.13

d = 0
deductions_1 = input('''Вы относитесь к льготной категории граждан или к лицам, 
на обеспечении которых находятся дети? ''')
if deductions_1.lower() == 'да' and days >= 183:
    print('У Вас могут быть вычеты')
    q_1 = input('Вы относитесь к 1-ой категории? ')
    q_2 = input('Вы относитесь ко 2-ой категории? ')
    if q_1.lower() == 'да':
        d += 3000
    else:
        d = 0
    if q_2.lower() == 'да':
        d += 500
    else:
        d = 0
    q_3 = input('''Вы являетесь родителем, супругом (супругой) родителя,
    усыновителем, на обеспечении которого находится ребенок? ''')
    if q_3.lower() == 'да':
        q_4 = input('Начиная с месяца, указанный доход превысил 350 000 рублей? ')
        q_7 = int(input('Сколько детей в Вашей семье?'))
        if q_4.lower() == 'да':
            print('Налоговый вычет, предусмотренный настоящим подпунктом, не применяется')
        if q_4.lower() == 'нет':
            q_5 = input('''Вашему ребенку до 18 лет и является ребенком-инвалидом
            или является учащимся очной формы обучения, аспирантом, ординатором, интерном, студентом в возрасте до 24 лет,
            или  он является инвалидом I или II группы? ''')
            if q_5.lower() == 'да':
                d += 12000 * q_7
            if q_5.lower() == 'нет':
                if q_7 == 1 or q_7 == 2:
                    d += 1400
                if q_7 >= 3:
                    d += 3000
                    print(f'Ваш вычет для льготных категорий граждан, а также лиц, на обеспечении которых находятся дети составляет {d}')
    if q_3.lower() == 'нет':
        q_5 = input('''Вашему ребенку до 18 лет и является ребенком-инвалидом
        или является учащимся очной формы обучения, аспирантом, ординатором, интерном, студентом в возрасте до 24 лет, 
        или  он является инвалидом I или II группы? ''')
        if q_5.lower() == 'да':
            d += 6000 * q_7
        if q_5.lower() == 'нет':
            if q_7 == 1 or q_7 == 2:
                d += 1400
            if q_7 >= 3:
                d += 3000
                print(f'Ваш вычет для льготных категорий граждан, а также лиц, на обеспечении которых находятся дети составляет {d}')

q_8 = input('''Являетесь ли Вы лицом, совершающим операции по ИИС
и получающим доходы от реализации ценных бумаг, обращающихся на ОРЦБ? ''')
if q_8.lower() == 'да' and days >= 183:
    print('''Будем считать вычет в размере дохода, полученного от продажи ценных бумаг (1)
    или вычеты по ИИС (2)''')
    opt = int(input('Выберите вариант ответа (1 или 2) '))
    if opt == 1:
        income_investments_1 = input('''Ваши ценные бумаги, обращающиеся на российских биржах,
        либо паи открытых ПИФов под управлением отечественных компаний? ''')
        if income_investments_1.lower() == 'да':
            qs_1 = input('Ваш доход облагается НДФЛ? ')
            if qs_1.lower() == 'нет':
                qs_2 = input('Активы находятся в собственности непрерывно более 3 лет? ')
                qs_3 = int(input('Сколько лет Вы владеете этими акциями? '))
                profit_securities = float(input('Ваша прибыль от ценных бумаг: '))
                if qs_2.lower() == 'да':
                    if profit_securities * 0.13 >= 3_000_000:
                        print('Вычет составит {3_000_000 * qs_3}')
                    if profit_securities * 0.13 < 3_000_000:
                        print('''Вычет в размере дохода, 
                        полученного от продажи ценных бумаг составит {profit_securities * 0.13}''')
                if qs_2.lower() == 'нет':
                    print('Вычета нет')
            if qs_1.lower() == 'да':
                print('Вычета нет')
        if income_investments_1.lower() == 'нет':
            print('Вычета нет')
    if opt == 2:
        tax_paid = float(input('Ваш налог равен '))
        personal_income_tax = int(input('Сколько процентов НДФЛ Вы платите? '))
        income = float(input('Ваш доход: '))
        replenishment = float(input('Сумма пополнения на ИИС: '))
        if tax_paid > replenishment * 0.13:
            print(f'Налоговый вычет по ИИС составляет 52_000')
        if tax_paid < replenishment * 0.13:
            print(f'Налоговый вычет по ИИС составляет {replenishment * 0.13}')
        if income >= 5_000_000 and personal_income_tax == 15:
            print(f'Налоговый вычет по ИИС составляет 60_000')
    else:
        print('Такого варианта нет')
if q_8.lower() == 'нет':
    print('Инвестиционные налоговые вычеты равны 0')

total_stoppage = stoppage + d
print(f"Ваш доход за год составил {t_income} руб.")
print(f"НДФЛ за год составил {t_tax} руб.")
print(f"Налоговый вычет за год составит {total_stoppage} руб.")
