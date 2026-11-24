
# Simple Calculator Project

print("===== PYTHON CALCULATOR =====")

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Choose an operation (1-5): ")

    if choice == "5":
        print("Thank you for using the calculator!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Try again.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = num1 + num2
        print("Result:", result)

    elif choice == "2":
        result = num1 - num2
        print("Result:", result)

    elif choice == "3":
        result = num1 * num2
        print("Result:", result)

    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Cannot divide by zero!")

# import math 
# print('====PYTHON CALCULATOR=====')

# while True:
#     print("\n 1.Addition")
#     print("2. Substraction")
#     print("3.Multiplication")
#     print("4. Division")
#     print("5.modulus")
#     print("6.power")
#     print("7.sqrt")
#     print("8. Exit")

#     choice = input("choose an operation (1-8):")
    
#     if choice =="8":
#         print("Thank you for using the calculator")
#         break
#     if choice not in ["1","2","3","4","5","6","7","8"]:
#         print("invalid choice ! try again")
#         continue

#     num1 = float(input("Enter first number"))
#     num2 = float(input("Enter seconf number"))

#     if choice =="1":
#         reslut= num1 + num2
#         print("Result:",reslut)
#     elif choice=="2":
#         reslut= num1 - num2
#         print("Result:",reslut)
#     elif choice=="3":
#         reslut = num1 * num2
#         print("Result:",reslut)
#     elif choice=="4":
#         if num2 != 0:
#             reslut = num1 / num2
#             print("Result",reslut)
#         else:
#             print("Error : cannot divide by zero")
#     elif choice=="5":
#         reslut = num1 % num2
#         print("Result",reslut)
#     elif choice =="6":
#         reslut = num1 ** num2
#         print("Result",reslut)
#     elif choice=="7":
#         reslut = math.sqrt(num1+num2)
#         print("reslut",reslut)