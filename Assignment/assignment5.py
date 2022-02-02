'''Write a program to rotate the value of x, y, z such that x has the value of y, y has the value of z and z has the value of x.'''
x = int(input("Enter the value of x\t"))
y = int(input("Enter the value of y\t"))
z= int(input("Enter the value of z\t"))

print("Before Swapping X Y Z is ",x ,y ,z)

temp = x
x = y
y = z
z = temp


print("After Swapping X Y Z is ",x ,y ,z)
