
#using loop

def even_loop(nums):
    odd =[]
    for i,v in enumerate(nums):
        if(v % 2 != 0):
            odd.append(v)

    return odd

#method 2 : list comprehensing 
def even_compren(nums):
    return [n for n in nums if n % 2 != 0]

print(even_loop([3,4,6,7,9,12,10,1]))
print(even_compren([3,4,6,7,9,12,10,1]))