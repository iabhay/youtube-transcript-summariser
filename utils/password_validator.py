import re


def password_validation(password):
    pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,20}$"
    answer = re.match(pattern, password)
    if answer:
        return True
    else:
        return False