import datetime
from datetime import datetime
from dateutil import relativedelta


def bonus_calculation(start_date_str, sick_leave_last_date_str=None):
    start_date = convert_string_to_date(start_date_str)
    sick_leave_last_date = convert_string_to_date(sick_leave_last_date_str)
    validate_input_parameters(start_date, sick_leave_last_date)
    experience_bonus = calculate_bonus_start_date(start_date)
    if experience_bonus == 0:
        return 0
    else:
        return experience_bonus + calculate_bonus_sick_leave(sick_leave_last_date)


def convert_string_to_date(date_string):
    if date_string is None:
        return None
    try:
        return datetime.strptime(date_string, "%d/%m/%Y")
    except(TypeError, ValueError):
        raise Exception("Please correct the data, it should be in format %d/%m/%Y")


def validate_input_parameters(start_date, sick_leave_last_date=None):
    if start_date > datetime.today():
        raise Exception("The person hasn't been hired yet!")

    if sick_leave_last_date:
        if sick_leave_last_date > datetime.today():
            raise Exception("Date of sick leave cannot be in the future!")
        if sick_leave_last_date < start_date:
            raise Exception("Date of sick leave cannot be before the hiring date!")


def calculate_bonus_sick_leave(sick_leave_last_date=None):
    if sick_leave_last_date:
        last_sick_year = relativedelta.relativedelta(datetime.today(), sick_leave_last_date).years
        if last_sick_year == 0:
            return 0
    return 3


def calculate_bonus_start_date(start_date):
    working_period = relativedelta.relativedelta(datetime.today(), start_date)
    if working_period.years > 3 or\
            (working_period.years == 3 and (working_period.months or working_period.days)):
        return 30
    elif (working_period.years == 1 and working_period.months >= 6) or\
            (working_period.years >= 2):
        return 25
    elif (datetime.today() - start_date).days >= 90:
        return 15
    else:
        return 0
