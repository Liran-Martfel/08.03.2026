import random

def get_lucky_numbers() -> tuple:
    amount = []
    for i in range (3):
        luck_number = random.randint(1,100)
        amount.append(luck_number)
    amount = tuple(amount)
    return amount
amount_ = get_lucky_numbers()
print(amount_)

def input_until_lucky(amount: tuple) -> int:
    tries = 0
    while True:
        try:
            lucky_number = int(input('enter A number: '))
            tries += 1
            if lucky_number < 1:
                print('try positive numbers')
                continue
            if lucky_number in amount:
                print(f'luckey_number! {lucky_number}, you tried {tries} times')
                return lucky_number

        except ValueError:
            print('need positive integer, not str, try again')

print(input_until_lucky(amount_))