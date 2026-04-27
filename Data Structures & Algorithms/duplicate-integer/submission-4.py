import numpy as np
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = np.sort(nums)
        n = len(sorted_nums)
        for i in range(n-1):
            if sorted_nums[i] == sorted_nums[i+1]:
                return True
            else:
                continue
        return False
        