class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for k, v in enumerate(nums):
            diff = target - v
            if diff in indices and k != indices[diff]:
                return[indices[diff], k]
            indices[v] = k
        return []