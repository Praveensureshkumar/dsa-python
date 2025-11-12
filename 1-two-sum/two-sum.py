class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        see={}
        for idx, num in enumerate(nums):
            find=target-num
            if find in see:
                return [see[find],idx]
            else:
                see[num]=idx
        


