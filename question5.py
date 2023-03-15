# Find duplicates in an array

def duplicates(arr):
    unique_ele= set()
    duplicate_ele = []
    for i in arr:
        if i in unique_ele:
            duplicate_ele.append(i)
        else:
            unique_ele.add(i)
            
    return duplicate_ele
l = [1, 2, 3, 2, 1, 4, 5, 4]
print(duplicates(l))