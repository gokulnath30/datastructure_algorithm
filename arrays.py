#%%
"""
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

"""
nums = [3,3]
target= 6
_len = len(nums)

for i in range(0,_len-1):
    for j in range(i+1,_len):
        # if nums[i]+nums[j] == target:
        #     print(i,j)
        print
            

