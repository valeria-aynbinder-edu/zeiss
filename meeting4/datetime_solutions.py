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



print(weekday_in_3_days("2021-12-08, Wed, 10:00"))
print(weekday_in_3_days("2021-12-01, Wed, 08:15"))
print(weekday_in_3_days("2021-12-02, Tue, 07:24"))