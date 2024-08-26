# write a python program to calculate factorial of input number.
num=int(input("enter the any number:"))
i=1
fact=1
while(i<=num):
    fact=fact*i
    i=i+1
    
print("factorial of",fact)