#https://robocontest.uz/tasks/0202
#Gugurt donalari va raqamlar

n = input()
hisob = 0
gugurt = {
    '0': 6,
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6
}
for i in n:
    if i in gugurt:
        hisob += gugurt[i]
print(hisob)