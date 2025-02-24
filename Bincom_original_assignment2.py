from Faerie_db import postgres_database
from todolist import todo
from babynamedatabase import finalbabynames

def fibonacci_generator():
    a = 0
    b = 1
    print(a, b)
    while a <= 100 and b <= 100:
        a = a + b
        print(a)
        b = a + b
        print(b)


fibonacci_generator()
postgres_database()
todo()
finalbabynames()
