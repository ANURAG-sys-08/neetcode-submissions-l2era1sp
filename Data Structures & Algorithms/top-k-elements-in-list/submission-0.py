class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for elem in nums:
            if elem not in hash:
                hash[elem] = 0
            if elem in hash:
                hash[elem] += 1
        arr = []
        for num, cnt in hash.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res