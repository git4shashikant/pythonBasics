import os
import pathlib

# use dir to see all the functions available in any module
print(f'Available functions: {dir(os)}')

print(f'Current directory: {pathlib.Path(os.curdir).absolute()}')

os.chdir('C:\\Users\\shasha\\PycharmProjects\\Basics')
print(f'Current changed directory: {pathlib.Path(os.curdir).absolute()}')

# changing back to previous directory
os.chdir('C:\\Users\\shasha\\PycharmProjects\\Basics\\fundamentals')
print(f'Current changed directory back to previous: {pathlib.Path(os.curdir).absolute()}')
