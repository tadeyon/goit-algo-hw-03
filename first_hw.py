from datetime import datetime

def get_days_from_today(date):
    today = datetime.today()

    try:
        date = datetime.strptime(date, "%Y-%m-%d")
    except:
        print("Incorrect input format!")

    result = (today - date).days
    return result