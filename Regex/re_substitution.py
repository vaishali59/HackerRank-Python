import re

#Squaring numbers
def square(match):
    print(match)
    number = int(match.group())
    print(number)
    return str(number**2)

print(re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9"))
