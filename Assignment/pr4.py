'''Write a program to swap two numbers using bitwise operators.'''

var1 = int(input("Enter Variable 1\t"))
var2 = int(input("Enter Variable 2\t"))

print("Before swapping Variable Values are ",var1 ,var2)

var1 = var1 ^ var2
var2 = var1 ^ var2
var1 = var1 ^ var2

print("Swapped Variable Values are ",var1 ,var2)