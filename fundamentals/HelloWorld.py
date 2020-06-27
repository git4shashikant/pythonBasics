# By default print ends with \n
# __name__ variable is passed equals to fileName if imported or default else main() if main is defined.

import platform

word = ''

while word != 'secret':
    word = input('Please input password: ')
print("Login successful")
print(50 * "-")
print("Value in built variable name is:  ", __name__)
print("Start Hello World with trailing new line")
print("HelloWorld with trailing exclamation", end='!')
print(" same line HelloWorld with trailing new line")
print("HelloWorld End")
print("Python version: {}".format(platform.python_version()))
print(50 * "-")





