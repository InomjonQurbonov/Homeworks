#https://robocontest.uz/tasks/0119
#Azimjonning qo'ylari

n = int(input())
if n % 2 == 1 or n <= 2:
  print("-1")
else:
  print(n // 2)