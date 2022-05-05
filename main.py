# a, b, c, d, e = 5, 7, 10, 370, 20
#
# result = a + b
# print(result)
# result /= c
# print(result)
# print(type(result))
# print(round(result**2 * 10), "\n")
#
# print(result)
# result = int(result)
# print(result, type(result))
# print(result * d)
# print(d // e)
# print(d % e)
# print("")
#
# print(d > c and d < e)
# vl = bool(print(c > b or c >= e))
# print(type(vl))
# print(vl == 0, vl != 0)
#
# print("")
# phrase = f"London is the capital with {c} mil. citizens."
# print(type(phrase), phrase)
# print("10" in phrase)
import decimal

from num2words import num2words
from decimal import *
print(getcontext())

print("You can make a calculation. Enter numbers and arithmetical operator (+-*/) below:")
print("To exit print \"stop\".\n")

cycles = 0
result = 0
number_1 = ""
operator = ""
number_2 = ""
operators = ('+', '-', '*', '/')
while True:
    try:
        number_1 = input("Enter the first number: ")
        if number_1.lower() == "stop":
            break
        number_1 = Decimal(number_1)
    except Exception:
        while not number_1.isdigit():
            number_1 = input("Enter the first DIGIT: ")
        number_1 = Decimal(number_1)

    operator = input("Enter the operator: ")
    if operator.lower() == "stop":
        break
    while operator not in operators:
        operator = input("Enter the operator form '+', '-', '*', '/': ")

    try:
        number_2 = input("Enter the second number: ")
        if number_2.lower() == "stop":
            break
        number_2 = Decimal(number_2)
    except Exception:
        while not number_2.isdigit():
            number_2 = input("Enter the second DIGIT: ")
        number_2 = Decimal(number_2)

    try:
        if operator == "+":
            result = number_1 + number_2
        elif operator == "-":
            result = number_1 - number_2
        elif operator == "*":
            result = number_1 * number_2
        elif operator == "/":
            result = number_1 / number_2
        print("\nCalculating....")
    except ZeroDivisionError:
        print("\nCalculating....")
        print(f"---You cannot divide by 0---")

    cycles += 1

    result_in_words = num2words(result)
    result_in_words_2 = num2words((result), lang='ru')

    # print("\nCalculating....")
    print(f"The result is: {result} ({result_in_words.capitalize()})/({result_in_words_2.capitalize()})")
    print(f"Cycles {cycles}\n")

