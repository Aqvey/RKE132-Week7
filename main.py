import datetime
from hello import say_hello

hour = datetime.datetime.now().hour
name = input("Sisesta oma eesnimi: ")


say_hello(hour, name)

