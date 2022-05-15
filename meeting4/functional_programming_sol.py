# filter vowels
import datetime

VOWELS = 'aeiou'
s = "Hello World!"
print("".join(filter(lambda char: char not in VOWELS, s)))



# Autumn dates
dates = ['12-10-2021', '18-12-2021', '19-06-2021','23-11-2022']
print(list(filter(
    lambda date: not 9 <= date.month <= 11,
    map(lambda date_str: datetime.datetime.strptime(date_str, "%d-%m-%Y"), dates)
)))


