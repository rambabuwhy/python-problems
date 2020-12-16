#find two numbers 

def find_sum(nums,k):

    result= []
    left = 0
    right = len(nums)-1

    nums.sort()


    while left <= right:
        if nums[left] + nums[right] == k:
            result.append(nums[left])
            result.append(nums[right])
            return result
        elif nums[left] + nums[right] < k:
            left = left + 1
        elif nums[left] + nums[right] > k:
            right = right - 1

    return result



print(find_sum([5,5,10,15,1,7],20))




