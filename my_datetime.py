import datetime

now = datetime.datetime.now()

print(now.year) # Kuvab praeguse aasta
print(now.month) # Kuvab praeguse kuu numbri
print (now.day) # Kuvab kuupäeva numbri (1 - 31)
print(now.hour) # Kuvab praeguse tunni (0 - 23)

weekday = now.strftime("%a")
print(weekday)