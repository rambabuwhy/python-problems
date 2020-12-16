#bruteforce

def product_bruteforce(nums):
    
    left = 1
    result = []
    for itr in range(len(nums)):

        curr_product = 1
        for ele in nums[itr+1:]:
            curr_product = curr_product * ele
        
        result.append(curr_product*left)

        left = left * nums[itr]


    return result

#optimized

def product_optimized(nums):

    left = 1
    result = []
    for ele in nums:
        result.append(left)
        left = left * ele
    
    right = 1    
    for ele in range(len(nums)-1,-1,-1):
        result[ele] = result[ele]*right
        right = right * nums[ele]


    return result



print(product_bruteforce([1,2,3,4]))
print(product_optimized([1,2,3,4]))


