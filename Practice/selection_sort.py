
unsorted_arr = [4,34,54,33,23,1,5,3,114,345,2332,12,1,23,234,234,23423,3,6,67,4567,435,32]
arr2 = [567,4,3]

def find_lowest(arr):
    lowest = arr[0]
    lowest_index = 0
    for i in range(len(arr)):
        if arr[i] < lowest:
            lowest_index = i
    return lowest_index

def sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        num = arr.pop(find_lowest(arr))
        sorted_arr.append(num)
    return sorted_arr   

print(sort(unsorted_arr))