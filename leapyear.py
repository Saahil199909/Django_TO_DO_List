

def leapyearchecker(year):
    if (year % 4 == 0 and year % 100 !=0) or year % 400 ==0:
        print(year)
    else:
        print("Its not a leap year")

leapyearchecker(2003)


