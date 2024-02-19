class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        TC: O(n log n) for sorting
        """
        return sorted(s) == sorted(t)