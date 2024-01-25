# Functions with outputs

def format_name(f_name, l_name):
    """Take a first and last name and format it to return
    the title case version of the name"""   # doc string
    if f_name == "" or l_name == "":
        return ("Please fill in your first name, then your last name")
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"  # return knows it's the end of the function

print(format_name(input("what is your first name? "), input("what is your last name? ")))


# how many days in a month challenge


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month - 1]


year = int(input("Enter a year"))
month = int(input("Enter a month"))
days = days_in_month(year, month)
print(days)


