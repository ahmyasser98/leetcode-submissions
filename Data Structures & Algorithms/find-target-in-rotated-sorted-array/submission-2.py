class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pos = -1
        for i in range(len(nums)):
            if nums[i] == target:
                pos = i
        return pos