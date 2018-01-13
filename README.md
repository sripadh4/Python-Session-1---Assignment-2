# Python-Session-1---Assignment-2
List of numbers, output in a single line separated by commas, that are divisible by 7 but not by 5.

numbers = list(range(2000, 3201))
for i in numbers:
    if i % 7 == 0 and i % 5 != 0:
        print (i, end=", ")
