import re
def name_validator():
    ans = input("Name: ")
    if re.match(r"^[A-Z]{1}+[a-z]{1,16}$",ans):
        return ans
    else:
        return False
def product_validator():
    ans = input("Product: ")
    if re.match(r"^[a-z]{1,16}$",ans):
        return ans
    else:
        return False
def date_validator():
    ans = input("Date: ")
    if re.match(r"^\d{2}+\.+\d{2}+\.+\d{4}$",ans):
        return ans
    else:
        return False
def num_validator(call):
    print(call)
    ans = input("Num: ")
    if re.match(r"^\d{1,10}+\.+\d{1,4}$",ans):
        return ans
    else:
        return False