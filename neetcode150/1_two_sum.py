class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # TC: O(n^2) -- double for loop iter n times each
        # sliding window
        for i in range(len(nums)):
            # pointer increments
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
            
