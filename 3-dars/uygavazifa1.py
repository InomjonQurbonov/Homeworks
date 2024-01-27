#https://robocontest.uz/tasks/0229
#Koshi

a, b = map(int, input().split())
arifmetik = (a + b) / 2
geometrik = (a * b) ** 0.5
if arifmetik == geometrik:
    print(" = ")
elif arifmetik < geometrik:
    print(" < ")
else:
    print(" > ")