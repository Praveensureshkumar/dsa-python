class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            find_value=target-nums[i]
            if find_value in dic:
                return [dic[find_value],i]
            else:
                dic[nums[i]]=i