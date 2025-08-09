from datetime import date

today = date.today()

today_year = today.year

iso_year = today.isocalendar()[0]

print(iso_year)

