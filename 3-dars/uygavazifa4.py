#https://robocontest.uz/tasks/0138
#Isfandiyor algebra darsida

def calculate_function_value(n):
    result = n**5 + 8 * n**4 - 5 * n**3 + 3 * n**2 + n - 12
    return result

n = int(input())
result = calculate_function_value(n)
print(result)