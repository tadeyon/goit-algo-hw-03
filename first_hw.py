from datetime import datetime

def get_days_from_today(date):
    today = datetime.today()

    date = datetime.strptime(date, "%Y-%m-%d")

    result = (today - date).days
    return result

print(get_days_from_today("2024-6-28"))