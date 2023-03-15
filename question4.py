# In an array, Count Pairs with given sum

def pair_count(arr,sum):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] +arr[j] == sum:
                count +=1
    return count

arr = [1, 5, 7, -1, 5]
sum = 6
print(pair_count(arr,sum))