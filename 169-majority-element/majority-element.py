class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count =0
        for num in nums:
            if count ==0:
                candidate = num
            if num == candidate:
                count +=1
            else:
                count -=1
        return candidate
        # count and compare approach with T.C:O(n), Space:O(n)
##    def mejorityElement(self, nums:list[int]) -> int:
##        count = {}
##        for num in nums:
##            count[num] = count.get(num,0)+1
##        majority_element = len(nums)//2
##        for key,value in count.items():
##            if value>majority_element:
##                return key
    # approach 2, If an element appears more than n/2 times, then after sorting it must occupy the middle position.
##    def mejorityElement(self,nums):
##            nums.sort()
##            return nums[len(nums)//2]
    # using boyer-Moore Algorithm       
        