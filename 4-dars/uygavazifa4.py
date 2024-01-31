#https://robocontest.uz/tasks/0076
#Sovg’a

gnom = list(map(int, input().split()))
s = int(input())
tanga = sum(gnom)
if tanga < s:
  print(s - tanga)
else:
  print('0')