# Python Program to Check if a Number is a Palindrome
n=int(input("Enter the any number:"))

original_number=n
reversed_number=0

while(n>0):
  r=n%10
  reversed_number= reversed_number*10+r
  n=n//10
  
if original_number==reversed_number:
    print("the given number is palindrome.")
else:
    print("the given number is not palindrome.")
    
