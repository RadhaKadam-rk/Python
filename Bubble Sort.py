def bubbleSort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp

    return nums

nums = [3,4,1,2,7,9,5]
result = bubbleSort(nums)
print(result)