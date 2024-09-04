#    Write a program that inputs a number n and prints the sum of all of the numbers from 1 to n:


n= int(input("enter the any value:"))
sum=0
for i in range(1,n+1):
     sum=sum+i

print("the total sum is:"+str(sum))

# Write a program that creates a list with the following integers: 3, 5, 9, 3, 2, 9, 10. The program should iterate through the values in the list and print out each of the integers on separate lines.
n=[3, 5, 9, 3, 2, 9, 10]

for num in n:
    print(num)