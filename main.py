import ru_local as ru

# Kuznetsov Igor , Yadreeva Maria

total_w = 0
month = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
         "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

for num in range(12):
    print(ru.SALARY, f"{month[num]}: ", end='')
    total_w += float(input())

investing = float(input(ru.INVESTING))
deposits = float(input(ru.DEPOSIT))
max_key_rate = float(input(ru.MAX_KEY_RATE))
days = int(input(ru.DAYS))
