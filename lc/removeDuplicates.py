def removeDuplicates(nums):
    jj = 0
    for ii in range(len(nums)-1):
        if nums[jj] == nums[jj+1]:
            del nums[jj] 
        else:
            jj = jj+1

    return nums
