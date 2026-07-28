class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
                # sorting approach with O(nlogn)
##        nums.sort()
##        for i in range(1,len(nums)):
##            if nums[i] == nums[i-1]:
##                return True
##        return False


        # hashset approch with O(n)
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        