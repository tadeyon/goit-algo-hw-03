import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000:
        raise Exception("Min value supposed to be >= 1 and max value <= 1000!")
    if quantity < min or quantity > max:
        raise Exception("Quantity supposed to be between min and max!")
    
    result = []

    for i in range(quantity):
        result.append(random.randint(min, max))

    return list(sorted(set(result)))
        


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)