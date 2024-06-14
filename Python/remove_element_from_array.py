"""
Task: Remove specified element from array
115 / 115 test cases passed
Runtime: 35 ms
Memory Usage: 16.4 MB
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

nums = [3, 2, 2, 3]
val = 3
solution = Solution() 
k = solution.removeElement(nums, val)
print('Output k:', k)
print('Modified nums:', nums[:k] + ['_'] * (len(nums) - k))
