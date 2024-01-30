money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
count_month = 0
diff = 0
while money_capital + salary > spend:
    diff = abs(salary - spend)
    money_capital -= diff
    count_month += 1
    spend *= (increase + 1)
print("Количество месяцев, которое можно протянуть без долгов:", count_month)
