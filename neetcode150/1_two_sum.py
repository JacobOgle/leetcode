class SolutionBruteForce:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # TC: O(n^2) -- double for loop iter n times each
        # sliding window
        for i in range(len(nums)):
            # pointer increments
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
            
class SolutionBetter:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # TC: O(n) - two for loops doing n work each time. unnested
        map = {}

        n = len(nums)

        for i in range(n):
            map[nums[i]] = i
        
        for i in range(n):
            compl = target - nums[i]
            if compl in map and map[compl] != i:
                return i, map[compl]
