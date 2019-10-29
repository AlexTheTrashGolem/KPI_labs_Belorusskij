a = int(input("Введите а "))
b = int(input("Введите b "))
answer = 0
for x in range((a // 2) * 2 + 1, b + 1, 2):
    answer += x**2
print(answer)
