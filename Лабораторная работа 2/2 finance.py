import math

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

total_deficit = 0
current_spend = spend

for month in range(months):
    if month > 0:
        current_spend *= (1 + increase)
    monthly_deficit = current_spend - salary
    total_deficit += monthly_deficit

money_capital = math.ceil(total_deficit)
print(money_capital)
