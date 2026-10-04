a = float(input("enter first number:"))
b = float(input("enter second number:"))
operator = input("enter the operators (=,-,*,/):")
if operator == "+":
    print(a+b)
elif operator == "-":
    print(a-b)
elif operator == "*":
    print(a*b)
elif operator == "/":
    print(a/b)
else:
    print("invalid operatotr")                