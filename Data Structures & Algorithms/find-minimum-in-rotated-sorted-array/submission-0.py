class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            num = sorted(nums)
            return num[0]
