# Calculator
Калькулятор денег и калорий.  
Калькулятор денег умеет:  
- сохранять новую запись методом add_record();
- считать сколько потрачено сегодня методом get_today_stats();
- определять сколько ещё денег можно потратить в рублях, долларах или евро: get_today_cash_remained();
- считать сколько денег потрачено за последние 7 дней: get_week_stats().
  
Калькулятор калорий умеер:  
- сохранять новую запись методом add_record();
- считать сколько съедено сегодня методом get_today_stats();
- определять сколько ещё можно съесть: get_today_calories_remained();
- считать сколько съедено за последние 7 дней: get_week_stats().
  
Пример:  
cash_calculator = CashCalculator(1000)  
cash_calculator.add_record(Record(amount=145, comment="кофе"))  
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))  
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))  
print(cash_calculator.get_today_cash_remained("rub"))  
Вывод: На сегодня осталось 555 руб
