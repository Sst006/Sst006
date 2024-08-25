print("Operations:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
n = input("Select one from above (1/2/3/4): ")

num1 = int(input("Enter the first no."))
num2 = int(input("Enter the second no."))

if n == "1":
    Addition=num1+num2
    print("The answer is:",Addition)
    
if n == "2":
    Subtraction=num1-num2
    print("The answer is:",Subtraction)
    
if n == "3":
    Multiplication=num1*num2
    print("The answer is:",Multiplication)
    
if n == "4":
    Division=num1/num2
    print("The answer is:",Devision)


    