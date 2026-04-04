class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        res = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                res = res*nums[j]
            output.append(res)
            res = 1
        return output