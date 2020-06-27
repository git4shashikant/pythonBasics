string = "StringFunctions"
print("string[0]: " + string[0])
print("string[6]:" + string[6])
print("string[6:14]:" + string[6:14])
if "Func" in string:
    print("Func is contained in string variable.")

if "Funk" not in string:
    print("Funk is not contained in string variable.")

# string formatting
digit = 12
print('String format example: %s %d' % (string, digit))

print('usage of replace(): ' + string.replace('Functions', 'Variable'))
print('usage of upper(): ' + string.upper())
print('usage of lower(): ' + string.lower())

string = string.replace('Functions', ',Functions')
listTemp = string.split(',')
print('split list pop: ' + listTemp.pop())
print('split list pop: ' + listTemp.pop())

print(":".join(string))
print(''.join(reversed(string)))

print("String strip function usage: ", "***welcome******".strip("*"))
print("String char count: ", "welcome".count('e'))
print("String length: ", len("welcome"))
print("welcome".__eq__("welcome"))
print(''.join(reversed("Hello World!")))
print("Hello World!"[::-1])
print("Hello World!".swapcase())
