import re

def password_validation(password):
    pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,20}$"
    answer = re.fullmatch(pattern, password)
    if answer:
        return True
    else:
        return False


def username_validation(username):
    pattern = "^([A-z0-9@_\-\.]{4,20})"
    answer = re.fullmatch(pattern, username)
    if answer:
        return True
    else:
        return False

def url_validation(url):
    pattern = "(https:\/\/)?(www.)?youtube.(com)\/watch\?v=[a-zA-Z0-9\-\_]{4,}"
    answer = re.fullmatch(pattern, url)
    if answer:
        return True
    else:
        return False
