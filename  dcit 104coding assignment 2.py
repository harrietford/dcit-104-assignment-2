import numbers
from re import I, X
from tkinter import Y

#sum of prime numbers less than n
n=int(input("enter a number:"))
n=int(n)
sum=0
for i in range(2,n+1):
    for j in range(2,i) :
            if i % j == 0: 
                break
            else:
                 print(i,"is prime")
                 sum=sum+i
print("sum of prime number is",sum)                  
        



    
    
    
        

