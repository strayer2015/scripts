def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    midpoint = int(len(nums)/2)
    #print(midpoint, nums[midpoint])
    if midpoint == 0:
        return int(nums[0] < target)
    elif nums[midpoint] == target:
        return midpoint
    elif nums[midpoint] > target:
        #print(nums[:midpoint], target, midpoint)
        return searchInsert(nums[:midpoint], target)
    else:
        #print(nums[midpoint:], target, midpoint)
        return searchInsert(nums[midpoint:], target) + midpoint

