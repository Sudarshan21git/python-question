# write a prograrm to test input number is armstrong or not.
num=int(input("enter the any number:"))
arm=0
c=num
while(num>0):
    r=num%10
    arm=arm+(r ** 3)
    num=num //10
    
if arm==c:
    print("the given number is armstrong number:")
else:
    print("The given number is not armstrong number")