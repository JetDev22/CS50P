expression = input("Expression: ").split()

if expression[1] == "+":
    print(round(float(expression[0])+float(expression[2]),1))
elif expression[1] == "-":
    print(round(float(expression[0])-float(expression[2]),1))
elif expression[1] == "/":
    print(round(float(expression[0])/float(expression[2]),1))
elif expression[1] == "*":
    print(round(float(expression[0])*float(expression[2]),1))
