num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** 3)
    temp = temp // 10
    
if num == sum:
    
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")
    
    
    
    
    
    num = 1675
    count = 0
    while num > 0:
        
    num = num // 10
    count = count + 1
    print(f"The number has {count} digit")
    num = 1