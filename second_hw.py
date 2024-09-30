import random

def get_numbers_ticket(min, max, quantity):
    
    result = []

    if min < 1 or max > 1000:
        return result
    
    if quantity <= 0:
        return result

    for i in range(quantity):
        result.append(random.randint(min, max))

    return sorted(set(result))