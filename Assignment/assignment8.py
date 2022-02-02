'''Write a program to accept the principal amount, rate of interest, and duration from the user, hence, to display interest amount and the total amount (principal +interest).'''

pa = int(input("Enter the principal Amount\t"))
roi = float(input("Enter the Rate of interst\t"))
duration = int(input("Enter the duration\t"))

interest = (pa *roi * duration) /100

print("Interest amount is ",interest)
print("total amount is ",interest+pa)


