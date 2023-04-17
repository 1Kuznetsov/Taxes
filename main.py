import ru_local as ru

# Kuznetsov Igor , Yadreeva Maria

t_salary = 0
t_tax = 0
t_income = 0
tax_lottery = 0
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

prize = float(input(ru.PRIZE))
prize_ad = float(input(ru.PRIZE_AD))

investing = float(input(ru.INVESTING))

deposits = float(input(ru.DEPOSIT))
max_key_rate = float(input(ru.MAX_KEY_RATE))
if deposits <= 1_000_000 * max_key_rate:
    print("Налог уплачивать не нужно")
else:
    tax_d = (deposits - 1_000_000 * max_key_rate) * 0.13
    print(f"Налог составит {tax_d} рублей")
    t_tax += tax_d

estate = float(input(ru.ESTATE))
if resident:
    special = input(ru.SPECIAL).lower()
    if special == "да":
        pass
    else:
        t_tax += 0.13 * estate
else:
    t_tax += 0.3 * estate

t_income += t_salary + investing + deposits + prize + prize_ad
t_income += estate + rent
