#faulty calculator

num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
op = input("enter operator:+ - * / ")


if num1 == 45 and num2 == 3 and op == "*":
    print("555")

elif num1 == 56 and num2 == 9 and op == "+":
    print("77")

elif num1 == 56 and num2 == 6 and op == "/":
    print("4")

elif op == "+":
    plus = num1+num2
    print(plus)
elif op == "-":
    sub = num1-num2
    print(sub)
elif op == "*":
    multi = num1*num2
    print(multi)
elif op == "/":
    div = num1+num2
    print(div)
else:
    print("unexpected")



