#https://robocontest.uz/tasks/0145
#Uchburchak

def find_largest_triangle(N, lengths):
    lengths.sort(reverse=True) 
    for i in range(N - 2):
        a, b, c = lengths[i], lengths[i + 1], lengths[i + 2]
        if a < b + c:
            return f"{c} {b} {a}"
    return "-1"
N = int(input())
lengths = list(map(int, input().split()))
result = find_largest_triangle(N, lengths)
print(result)