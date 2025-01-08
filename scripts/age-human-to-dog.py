def age_dog(age_human):
    if age_human <= 0:
        return "age no valid"
    elif age_human <= 2:
        return age_human * 10.5
    else:
        return 21 + (age_human - 2) * 4

age_human = int(input("age"))
print("age dog:", age_dog(age_human))