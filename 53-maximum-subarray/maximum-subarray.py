class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        result=0
        for i in nums:
            result+=i
            if result > max_sum:
                max_sum=result
            if result <0:
                result=0
        return max_sum


        