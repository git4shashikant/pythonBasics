
mixed = {"Name": "Shashi Kant", "Tech": ["Java", "Python", "JS"], "Roles": {"HKNG": "Tech Lead", "PTP": "Dev"}, "Desc": "Extraordinary performance."}
print(mixed)

for mix in mixed:
    value = mixed[mix]
    if isinstance(value, str):
        print("String, {}: {}".format(mix, value))
    elif isinstance(value, tuple):
        print("Tuple, {}: {}".format(mix, value))
    elif isinstance(value, list):
        print("List, {}: {}".format(mix, value))
    elif isinstance(value, set):
        print("Set, {}: {}".format(mix, value))
    elif isinstance(value, dict):
        print("Dict, {}: {}".format(mix, value))
    else:
        print("Data type not supported.")

