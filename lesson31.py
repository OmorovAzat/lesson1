from datetime import date, datetime, timedelta
import locale

# #date
#
#
# today = date.today()
# print(today)
# print(today.day)
# print(today.month)
# print(today.year)
# print(today.weekday())
#
# #datetime

now = datetime.now()
# now2 = datetime.today()

# print(now)
# print(now.day)
# print(now.month)
# print(now.year)
# print(now.weekday())
# print(now.hour)
# print(now.minute)
# print(now.second)

# days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
# print(days[now.weekday()])

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

# now = datetime.now()
# print(now)
#
# print(now.strftime('%a'))
# print(now.strftime('%A'))
#
# print(f'Дата: {now.strftime("%A, %d %b %Y")}')
# print(f'Время: {now.strftime("%H: %M:%S")}')
#
# print(now.strftime('%c'))
# print(now.strftime('%x'))
# print(now.strftime('%X'))


now = datetime.today()
print(now. strftime('%c'))
d1 = now + timedelta(days=1, hours=2, minutes=10)
print(d1.strftime('%c'))