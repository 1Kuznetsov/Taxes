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
    question_1 = input(ru.QUESTION_1)
    question_2 = input(ru.QUESTION_2)
    if question_1.lower() == 'нет' and question_2.lower() == 'нет':
        print("Вы нерезидент, налоговые вычеты не предоставляются")
    if question_1.lower() == 'да' and question_2.lower() == 'да':
        print(f'Вы резидент, Ваш налог составляет {t_income}')
    dividends = input(ru.DIVIDENTS)
    if dividends.lower() == 'да':
        n_div = float(input(ru.N_DIV))
        tax_dividends = n_div * 0.15
    else:
        tax_dividends = 0
    tax_dep = 0
    if max_key_rate * 10_000 < deposits:
        tax_dep = 0
    else:
        tax_dep += deposits * 0.13
    property_non_resident = property_t1 + property_t2 + property_t3 + estate
    question_3 = input(ru.QUESTION_3)
    question_4 = input(ru.QUESTION_4)
    question_5 = input(ru.QUESTION_5)
    question_6 = input(ru.QUESTION_6)
    question_7 = input(ru.QUESTION_7)
    question_8 = input(ru.QUESTION_8)
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
deductions_1 = input(ru.DEDUCTION_1)
if deductions_1.lower() == 'да' and days >= 183:
    print('У Вас могут быть вычеты')
    q_1 = input(ru.Q_1)
    q_2 = input(ru.Q_2)
    if q_1.lower() == 'да':
        d += 3000
    else:
        d = 0
    if q_2.lower() == 'да':
        d += 500
    else:
        d = 0
    q_3 = input(ru.Q_3)
    if q_3.lower() == 'да':
        q_4 = input(ru.Q_4)
        q_7 = int(input(ru.Q_7))
        if q_4.lower() == 'да':
            print('Налоговый вычет, предусмотренный настоящим подпунктом, не применяется')
        if q_4.lower() == 'нет':
            q_5 = input(ru.Q_5)
            if q_5.lower() == 'да':
                d += 12000 * q_7
            if q_5.lower() == 'нет':
                if q_7 == 1 or q_7 == 2:
                    d += 1400
                if q_7 >= 3:
                    d += 3000
                    print(f'Ваш вычет для льготных категорий граждан, а также лиц, на обеспечении которых находятся дети составляет {d}')
    if q_3.lower() == 'нет':
        q_5 = input(ru.Q_5)
        if q_5.lower() == 'да':
            q_7 = int(input(ru.Q_7))
            d = d + 6000 * q_7
        if q_5.lower() == 'нет':
            q_7 = int(input(ru.Q_7))
            if q_7 == 1 or q_7 == 2:
                d += 1400
            if q_7 >= 3:
                d += 3000
                print(f'Ваш вычет для льготных категорий граждан, а также лиц, на обеспечении которых находятся дети составляет {d}')

q_8 = input(ru.Q_8)
if q_8.lower() == 'да' and days >= 183:
    print('''Будем считать вычет в размере дохода, полученного от продажи ценных бумаг (1)
    или вычеты по ИИС (2)''')
    opt = int(input(ru.OPT))
    if opt == 1:
        income_investments_1 = input(ru.INCOME_INVESTMENTS_1)
        if income_investments_1.lower() == 'да':
            qs_1 = input(ru.QS_1)
            if qs_1.lower() == 'нет':
                qs_2 = input(ru.QS_2)
                qs_3 = int(input(ru.QS_3))
                profit_securities = float(input(ru.PROFIT_SECURITIES))
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
        tax_paid = float(input(ru.TAX_PAID))
        personal_income_tax = int(input(ru.PERSONAL_INCOME_TAX))
        income = float(input(ru.INCOME))
        replenishment = float(input(ru.REPLENISHMENT))
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
