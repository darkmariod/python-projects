from datetime import date 

def calc_age(birth_date):
    age = int((date.today() -birth_date).days / 365.24)
    return age

print(calc_age(date(2000, 1, 1)))
