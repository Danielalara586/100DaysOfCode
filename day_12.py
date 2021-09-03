# Day 12: Days Until Birthday

import datetime
now = datetime.date.today()

def birth_days(month, day, year):
    birthday = datetime.date(year, month, day).replace(year = now.year)
    
    if now < birthday:
        return (birthday - now).days
    else:
        return (birthday.replace(year = now.year + 1) - now).days


def run():
    print("Please enter your birthdate [MM/DD/YYYY]")
    month = int(input("Month -> "))
    day = int(input("Day -> "))
    year = int(input("Year -> "))
    days_until_bd = birth_days(month, day, year)
    print(f"Days until birthday: {days_until_bd}")


if __name__ == "__main__":
    run()