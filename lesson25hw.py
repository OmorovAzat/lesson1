from random import randint
attempts = 1
num = 100
num = randint(1, 100)
print("Загадано  число от 1 до 100")
ask = int(input("Ваш вариант?"))
while num != ask:
    if num > ask: print("Угадываемое число больше 'num' ")
    elif num < ask: print("Угадываемое число меньше 'ask'")
    attempts += 1
    ask = int(input("Ваш вариант - "))
print(f"вы угадали число {num} за {attempts} попыток")
print("Спасибо за игру")