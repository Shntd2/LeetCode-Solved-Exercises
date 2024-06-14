"""
Task: Remove Duplicates from Sorted Array
362 / 362 test cases passed
Runtime: 75 ms
Memory Usage: 17.8 MB
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        k = 1 
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]  
                k += 1        
        return k

nums = [0,0,1,1,1,2,2,3,3,4]
solution = Solution() 
k = solution.removeDuplicates(nums) 
print(k, nums[:k] + ['_'] * (len(nums) - k))
