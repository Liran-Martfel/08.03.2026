import random

def get_lucky_numbers(amount: int) -> tuple:
    lucky = []
    for i in range (amount):
        luck_number = random.randint(1,100)
        lucky.append(luck_number)
    lucky = tuple(lucky)
    return lucky
lucky = get_lucky_numbers(3)
print(lucky)

def input_until_lucky(lucky: tuple) -> int | None:
    tries = 0
    while True:
        try:
            lucky_number = int(input('enter A number: '))
            tries += 1
            if lucky_number < 1:
                print('try positive numbers')
                continue
            if lucky_number in lucky:
                print(f'lucky_number! {lucky_number}, you tried {tries} times')
                return tries

        except ValueError:
            print('need positive integer, not str, try again')

input_until_lucky(lucky)