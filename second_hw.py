import random

def get_numbers_ticket(min, max, quantity):
    
    result = []

    if min < 1 or max > 1000 or min > max:
        return result
    
    if quantity <= 0 or quantity > (max - min + 1):
        return result

    result = random.sample(range(min, max + 1), quantity)

    return sorted(result)
