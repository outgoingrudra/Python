import math
num = int(input("Enter a Number :"))
sum = 0
l = int(math.log10(num))+1

t = num
while t:
    sum += (t%10)**l
    t = t//10
if sum == num :
    print("Armstrong Number !")
else :
    print("Not Armstrong Number !")