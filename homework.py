import datetime as dt


class Record:
    """Класс записи трат."""

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:
    """Родительский класс калькулятора калорий и денег."""

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.date.today()
        return sum(record.amount for record in self.records
                   if record.date == today)

    def get_week_stats(self):
        today = dt.date.today()
        week_ago = today - dt.timedelta(days=7)
        return sum(record.amount for record in self.records
                   if week_ago < record.date <= today)

    def remaining_limit(self):
        return self.limit - self.get_today_stats()


class CaloriesCalculator(Calculator):
    """"Класс калькулятора калорий."""

    def get_calories_remained(self):
        if self.remaining_limit() > 0:
            return ('Сегодня можно съесть что-нибудь ещё,'
                    f' но с общей калорийностью не более {self.remaining_limit()} кКал')
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):
    """Класс денежного калькулятора."""

    USD_RATE = 96.16
    EURO_RATE = 102.28
    RUB_RATE = 1

    def get_today_cash_remained(self, currency):
        limit_today = self.remaining_limit()
        curr_rate = {'usd': ('USD', self.USD_RATE),
                     'eur': ('Euro', self.EURO_RATE),
                     'rub': ('руб', self.RUB_RATE)}

        curr_name, curr_value = curr_rate[currency]
        if limit_today == 0:
            return 'Денег нет, держись'
        if currency not in curr_rate:
            return ValueError('Выбрана неверная валюта. Доступны только: "usd", "eur", "rub"')
        if limit_today < 0:
            return (f'Денег нет, держись: твой долг - {abs(round(limit_today / curr_value, 2))}'
                    f' {curr_name}')
        return (f'На сегодня осталось {abs(round(limit_today / curr_value, 2))}'
                f' {curr_name}')
