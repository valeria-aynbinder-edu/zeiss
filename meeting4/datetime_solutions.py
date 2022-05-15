import datetime

# "2021-12-08, Wed, 10:00"
def weekday_in_3_days(date_as_str):
    try:
        dt = datetime.datetime.strptime(date_as_str, "%Y-%m-%d, %a, %H:%M")
        new_date = dt + datetime.timedelta(days=3)
        # new_date.weekday()
        ret_val = new_date.strftime("%A")
        return ret_val
    except ValueError:
        print('Invalid format')


def isHoliday(date,*holidays):
    print(f"User Input is: {date}")
    try:
        print(f"Accepted format: {datetime.datetime.strptime(date, '%d-%m-%Y')}")
        userinput_datetime = datetime.datetime.strptime(date, '%d-%m-%Y')
        print(userinput_datetime)
        userinput_day = userinput_datetime.strftime('%a')
        if userinput_day in holidays:
            print(f"User's Input: {date} is a {userinput_day}, and is a Holiday ({holidays})")
            return True
        else:
            print(f"User's Input: {date} is a {userinput_day}, and is not a Holiday ({holidays})")
            return False
    except:
        print(f"Wrong Input")
        print(f"Provided input is: {date}")
        return Exception


# Exercise 1
print(weekday_in_3_days("2021-12-08, Wed, 10:00"))
print(weekday_in_3_days("2021-12-01, Wed, 08:15"))
print(weekday_in_3_days("2021-12-02, Tue, 07:24"))


#   Exercise 2
print("\n\n")
print("Exercise 2")
print("Format expected: dd-mm-yyyy") #  %d-%m-%Y
userinput = input("Please enter a date:" )
isHoliday(userinput, 'Fri', 'Sat')