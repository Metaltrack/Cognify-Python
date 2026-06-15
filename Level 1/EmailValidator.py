import re

def verify_mail(email :str):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        
    if re.match(regex, email):
        return True
    else:
        return False


