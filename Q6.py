# write t a program to test input number is perfect or not.
n=int(input("Enter the any number:"))

sum=0
for i in range(1,n):
    if(n%i==0):
     sum+=i
if(sum==n):
    print("The given number is perfect number.")
else:
    print("The given number is not perfect.")