import ru_local as ru

# Kuznetsov Igor , Yadreeva Maria

t_salary = 0
t_tax = 0
t_income = 0
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
if resident:
    t_tax += property_t1 * 0.001 + property_t2 * 0.02 + property_t3 * 0.005
else:
    t_tax += (property_t1 + property_t2) * 0.002 + property_t3 * 0.02

rent = float(input(ru.RENT))
if resident:
    t_tax += 0.13 * rent
else:
    t_tax += 0.3 * rent

investing = float(input(ru.INVESTING))

deposits = float(input(ru.DEPOSIT))
max_key_rate = float(input(ru.MAX_KEY_RATE))
if deposits > 1_000_000 * max_key_rate:
    t_tax += (deposits - 1_000_000 * max_key_rate) * 0.13

prize = float(input(ru.PRIZE))
prize_ad = float(input(ru.PRIZE_AD))

estate = float(input(ru.ESTATE))
if resident:
    special = input(ru.SPECIAL).lower()
    if special == "нет":
        t_tax += 0.13 * estate
else:
    t_tax += 0.3 * estate

t_income += t_salary + investing + deposits + prize + prize_ad
t_income += estate + rent

if days < 183:
    question_1 = input('Вы отсутствовали в стране по причинам прохождения лечения, n\
    обучения или исполнения за границей обязательств по трудовому договору? ')
    question_2 = input('Вы российский военнослужащий, который несет воинскую обязанность за границей n\
    или сотрудник органов власти в командировке за пределами РФ? ')
    if question_1.lower() == 'нет' and question_2.lower() == 'нет':
        print("Вы нерезидент, налоговые вычеты не предоставляются")
    dividends = input('Получали ли Вы дивиденды? ')
    if dividends.lower() == 'да':
        n_div = float(input('Какой доход от дивидентов? '))
        tax_dividends = n_div * 0.15
    else:
        tax_dividends = 0
    tax_dep = 0
    if max_key_rate * 10000 < deposits:
        tax_dep = 0
    else:
        tax_dep += deposits * 0.13
    property_non_resident = property_t1 + property_t2 + property_t3 + estate
    tax_non_resident = (investing + t_salary + rent + estate + prize_ad + prize) * 0.3
    tax_non_resident += tax_dividends + property_non_resident * 0.2 * 0.01 + tax_dep
    print(f'Ваш налог составляет {tax_non_resident}')