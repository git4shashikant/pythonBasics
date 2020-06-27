testDict = {'key1': 1, 'key2': 2, 'key3': 3}
print(testDict['key1'])

testDict.update({'key4': 4})
print('After adding key4: ' + str(testDict.items()))

del testDict['key1']
print('After deleting key1: ' + str(testDict.items()))

temp_dict = testDict.copy()
print(temp_dict.items())
print("length of dictionary: %d" % (len(temp_dict)))

# looping on dictionary
print("dict keys: " + str(testDict.keys()))
print("dict values: " + str(testDict.values()))
for key in testDict.keys():
    print("%s : %s" % (key, str(testDict[key])))

Students = list(testDict.keys())
Students.sort()
for key in Students:
    print(":".join((key, str(testDict[key]))))

print(type(testDict))
