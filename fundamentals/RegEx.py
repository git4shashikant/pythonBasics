import re

pattern = "^\w*"
name = "shashi kant"
match = re.findall(pattern, name)
print(match)

pattern = "\s"
match = re.split(pattern, name)
print(match)
