num = int(input("Enter Number :"))

for i in range(2,int(num**0.5)+1):
    if num%i==0:
        print("Not a Prime Number !")
        exit()
print(" Prime Number !")