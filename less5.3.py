from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет не больше 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите еще раз от 1 до 28: "))
    return x

def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось {value}.")
    
def bot_calc(value):
    k = randint(1,29)
    while value-k <= 28 and value > 29:
        k = randint(1,29)
    return k

player1=input('Имя первого игрока:')
player2="Bot"

value=int(input('введите общее количество конфет:'))

flag = randint(0,2)
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = bot_calc(value)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)
if flag:
    print(f"Победил {player1}")
else:
    print(f"Победил {player2}")