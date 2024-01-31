#https://robocontest.uz/tasks/0113
#Baho

grade = int(input())
if grade == 38:
    print('40')
elif grade < 38:
    print(grade)
else:
    remainder = grade % 5
    if remainder >= 3:
        print(grade + (5 - remainder))
    else:
        print(grade)