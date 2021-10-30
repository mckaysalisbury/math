def is_sorted1(a, b, c, d, e, f): 
    return a < b and b < c and c < d and d < e

def is_sorted(*a):
    # print(a,"sorted?")
    if len(a) <= 1:
        # print("yes")
        return True
    if a[0] > a[1]:
        # print("no")
        return False
    # print("don't know", a[1:])
    return is_sorted(*a[1:])
# print(is_sorted(1, 2, 3, 4))
# print(is_sorted(2, 1, 3, 4))
# print(is_sorted(1, 2, 3, 5, 6, 4))

def rotate(arr, index, direction = 1, number = 3):
    returnArray = [a for a in arr]
    # deal with up and down
    index = index if direction == 1 else index + number - 1
    # index = (direction % number - 1) * (number - 1) + index
    # print("idx", index)
    temp = returnArray[index]
    # print("saving", temp)
    while number > 1:
        # print("idx", index, "n", number)
        # print("copying ")
        returnArray[index] = returnArray[index + direction]
        number -= 1
        index += direction
    returnArray[index] = temp
    return returnArray

sorted = [1, 2, 3, 4]
# print(rotate(sorted, 1, 1))
# print(rotate(sorted, 1, -1))

# print(rotate(rotate(rotate(sorted, 0, 1), 0, 1), 0, 1))
operations = {
    'firstUp': lambda a: rotate(a, 0, 1),
    'firstDown': lambda a: rotate(a, 0, -1),
    'secondUp': lambda a: rotate(a, 1, 1),
    'secondDown': lambda a: rotate(a, 1, -1),
    'thirdUp': lambda a: rotate(a, 2, 1),
    'thirdDown': lambda a: rotate(a, 2, -1),
    'allUp': lambda a: rotate(a, 0, 1, 6),
    'allDown': lambda a: rotate(a, 0, -1, 6),
}
# print(operations)

def multiApply(input):
    return { name: operation(input) for name, operation in operations.items() }

def recursiveApply(input):
    returnValue = {}
    # print("unpack", input, input.values())
    for name, value in input.items():
        newValues = multiApply(value)
        for newName, newValue in newValues.items():
            returnValue[f"{name}.{newName}"] = newValue
            if is_sorted(*newValue):
                print("Found it!", name, newName);
    return returnValue

root = { 'root': [6,36,30,12,24,18] }

# for name, func in operations.items():
#      print(name, func(root['root']))


current = root
for i in range(4):
    print(i)
    current = recursiveApply(current)

