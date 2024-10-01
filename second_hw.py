import random

def get_numbers_ticket(min, max, quantity):
    
    result = []

    if not 1 <= min < max <= 1000:
        return result
    
    if quantity > (max - min + 1):
        return result

    result = random.sample(range(min, max + 1), quantity)

    return sorted(result)
