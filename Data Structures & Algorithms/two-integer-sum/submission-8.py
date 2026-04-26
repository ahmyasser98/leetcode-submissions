class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for k, v in enumerate(nums):
            diff = target - v

            if diff in indices and indices[diff] != k:
                return [indices[diff], k]
            
            indices[v] = k

        return []
