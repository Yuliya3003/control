array = [str(el) for el in input().split()]
new_array = []
for str in array:
    if len(str) <=3:
        new_array.append(str)

print(new_array)
