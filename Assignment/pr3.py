'''Write a program to swap the value of two variables using a third variable and without using a third variable.'''
var1 = int(input("Enter Variable 1\t"))
var2 = int(input("Enter Variable 2\t"))

print("Before swapping Variable Values are ",var1 ,var2)

x = var1
var1 = var2
var2 = x

print("Swapped Variable Values using third value are ",var1 ,var2)

print("Before swapping Variable Values are ",var1 ,var2)

var1=var1+var2   
var2=var1-var2  
var1=var1-var2

print("Swapped Variable Values without using third value are ",var1 ,var2)