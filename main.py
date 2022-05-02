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

from num2words import num2words
from decimal import Decimal

print("You can make a calculation. Enter numbers and arithmetical operator (+-*/) below: \n")

number_1 = Decimal(input("Enter the first number: "))
operator = input("Enter the operator: ")
number_2 = Decimal(input("Enter the second number: "))

if operator == "+":
    result = number_1 + number_2
elif operator == "-":
    result = number_1 - number_2
elif operator == "*":
    result = number_1 * number_2
elif operator == "/":
    result = number_1 / number_2

result_in_words = num2words(result)
result_in_words_2 = num2words(result, lang='ru')

print("\nCalculating....")
print(f"The result is: {result} ({result_in_words.capitalize()})/({result_in_words_2.capitalize()})")