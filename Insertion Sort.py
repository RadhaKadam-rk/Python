def insertionSort(nums):
    n = len(nums)
    for i in range(1,n):
        key = nums[i]
        j = i-1
        while j>=0 and nums[j]>key:
            nums[j+1] = nums[j]
            j -= 1
            nums[j+1] = key

    return nums

nums = [9,3,5,1,7,2,99,11,55,22,77,88,33,45,54,21,12,90,78,92]
result = insertionSort(nums)
print(result)