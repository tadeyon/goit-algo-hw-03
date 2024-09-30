import re

def normalize_phone(phone_number):
    phone_number = re.sub("\s+", "", phone_number)

    phone_number = re.sub(r"[^0-9+]","", phone_number)

    if re.compile(r"[^+]").match(phone_number, 0, 1):
        phone_number = re.sub(r"^", "+", phone_number)
    
    if re.compile(r"[^38]").match(phone_number, 1, 2):
        phone_number = re.sub(r"[+]", "+38", phone_number)

    return phone_number