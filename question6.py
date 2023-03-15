# Find the Kth largest and Kth smallest number in an array

def largest_smallest_num(arr,k):
    new_arr = sorted(arr)
    # print(new_arr)
    largest_num = new_arr[-k]                         # If i wanna find max out of arr, i'll use -1 as index. same as for kth last element [-k]
    smallest_num = new_arr[k-1]
    return f"kth largest number: {largest_num}\nkth smallest number: {smallest_num}"





l = [1,9,2,1,2,3,6,4,3]           # [1,1,2,2,3,3,4,6,9]
k = 3
print(largest_smallest_num(l,k))
