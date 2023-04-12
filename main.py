import ru_local as ru

# Kuznetsov Igor , Yadreeva Maria

t_salary = 0
t_tax = 0
t_income = 0
tax_lot = 0
month = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
         "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

for num in range(12):
    print(ru.SALARY, f"{month[num]}: ", end='')
    t_salary += float(input())

days = int(input(ru.DAYS))
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
t_income += t_salary + investing + deposits