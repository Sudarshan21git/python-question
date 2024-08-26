# write the program to test input number is prime or not
n=int(input("Enter the any number:"))

count=0
for i in  range(1,n+1):
    if(n%i==0):
        count+=1
        
if count==2:
    print("the given number is prime.")
else:
    print("the given number is not prime")