from datetime import date

d = date(2016, 1, 1)

today = d.today()

today_year = d.year

iso_year = d.isocalendar()[0]


print(iso_year)
print(today_year)

