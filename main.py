a, b, c, d, e = 5, 7, 10, 370, 20

result = a + b
print(result)
result /= c
print(result)
print(type(result))
print(round(result**2 * 10), "\n")

print(result)
result = int(result)
print(result, type(result))
print(result * d)
print(d // e)
print(d % e)
print("")

print(d > c and d < e)
vl = bool(print(c > b or c >= e))
print(type(vl))
print(vl == 0, vl != 0)

print("")
phrase = f"London is the capital with {c} mil. citizens."
print(type(phrase), phrase)
print("10" in phrase)


