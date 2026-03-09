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
    tries = 1
    try:
        lucky_number = int(input('enter A number: '))
        print(lucky_number)
    except ValueError:
        print('need positive integer, not str, try again')

    lucky_number = int(input('enter a number: '))
    if lucky_number < 1:
        print('try positive numbers')
        lucky_number = int(input('enter a number: '))
        tries += 1

    while lucky_number not in amount:
        lucky_number = int(input('enter a number: '))
        tries += 1

    else:
        print(f'lucky_number! {lucky_number}, you tried {tries} times')
        return lucky_number


print(input_until_lucky(amount_))