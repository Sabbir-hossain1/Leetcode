class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict[target - num], i]
            num_dict[num] = i

    def twoSumSorting(self, nums: list[int], target: int) -> list[int]:
        # First sort the array
        # take the first item and find the complement (target - first item) using binary search
        pass