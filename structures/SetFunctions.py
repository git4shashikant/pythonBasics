games = {"Cricket", "Soccer", "Hockey"}
games.add("Fuzeball")
games.add("Cricket")

sorted(games)
for game in games:
    print(game)


a = set("A set of characters.")
b = set("another set of chars")

# union
c = a | b
print("chars in a or b: {", end= "")
for i in c:
    print(i, end= "")
print("}")

# intersection
c = a & b
print("chars in a and b: {", end= "")
for i in c:
    print(i, end= "")
print("}")

# not common in both sets
c = a ^ b
print("chars in a and b: {", end= "")
for i in c:
    print(i, end= "")
print("}")

