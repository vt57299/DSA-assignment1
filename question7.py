# Move all the negative elements to one side of the array

def negative_to_one_side(arr):
    arr1 = []
    arr2 = []
    for i in range(len(arr)):
        if arr[i] < 0:
            arr1.append(arr[i])
        else:
            arr2.append(arr[i])
    arr1.extend([i for i in arr2])
    return arr1

l = [1,2,46,3,1,7,8,-45,-23,6,-34,74,-3]
print(negative_to_one_side(l))