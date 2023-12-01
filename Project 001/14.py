arr1 = [66, 20, 57, 34, 28, 98, 91, 46, 97, 77, 106, 85, 76, 91, 4, 101, 87, 21, 113, 105]
step = 1
arr2 = []
current_index = 0

while current_index < len(arr1):
    arr2.append(arr1[current_index])
    current_index = step + current_index
    step = step + 1

print(arr2)
