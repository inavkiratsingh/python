# 45 + 3 = 555, 56 + 9 = 77, 56/6 = 4
print("Welcome to calculator made by Navkirat")
print("Type following operator for calculate two no.")
print("'+' for addition")
print("'-' for subtraction")
print("'*' for multiplication")
print("'/' for division")
print("'**' for solve power")



operator = input("Enter operator ", )

first_no = int(input("Enter first number ",  ))
sec_no = int(input("Enter second number ",  ))



if first_no == 45 and sec_no == 3 and operator == '+':
    print(555)

elif first_no == 56 and sec_no == 9 and operator == '+':
    print(77)

elif first_no == 56 and sec_no == 6 and operator == '/':
    print(4)

elif operator == '+':
    print(first_no + sec_no)

elif operator == '-':
    print(first_no - sec_no)

elif operator == '*':
    print(first_no * sec_no)

elif operator == '**':
    print(first_no ** sec_no)

elif operator == '/':
    print(first_no / sec_no)

else:
    print("wrong way of calculation plsease enter a valid no. or operator")
