num = int(input("Yo diddy, enter a number: "))
count = 0
while num > 0:
    num = num // 10
    count = count + 1
print(f"The number you chose has {count} digit")
    