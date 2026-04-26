class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        sorted_items = sorted(count.items(), key=lambda item: item[1], reverse = True)
        for i in range(k):
            res.append(sorted_items[i][0])
        return res
             
        