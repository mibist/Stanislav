from datetime import datetime

class SuperDate(datetime):
    SEASONS = {
        'Winter': (1, 2, 12),
        'Spring': (3, 4, 5),
        'Summer': (6, 7, 8),
        'Autumn': (9, 10, 11)
    }

    TIME_OF_DAY = {
        'Morning': range(6, 12),
        'Day': range(12, 18),
        'Evening': range(18, 24),
        'Night': range(0, 6)
    }

    def get_season(self):
        for season, months in self.SEASONS.items():
            if self.month in months:
                return season

    def get_time_of_day(self):
        hour = self.hour
        for time, hours_range in self.TIME_OF_DAY.items():
            if hour in hours_range:
                return time

# Пример использования
# a = SuperDate(2024, 2, 22, 12)
# print(a.get_season())
# print(a.get_time_of_day())

# Функция для получения даты от пользователя
def get_user_date():
    while True:
        date_str = input("Введите дату в формате (год-месяц-день час:минута (ПРИМЕР: 2024-2-22 12:00)): ")
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
            return date
        except ValueError:
            print("Неверный формат. Пожалуйста, введите дату в правильном формате.")

# Пример использования с вводом с консоли
user_date = get_user_date()
super_date = SuperDate(user_date.year, user_date.month, user_date.day, user_date.hour, user_date.minute)
print("Сезон:", super_date.get_season())
print("Время суток:", super_date.get_time_of_day())