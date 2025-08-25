class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot=-1
        right=len(nums)-1

        while right>0:
            if nums[right-1]<nums[right]:
                pivot=right-1
                break
            right-=1

        if pivot == -1:
            left,right=0,len(nums)-1
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
            return nums

        next_value=0
        for i in range(len(nums)-1,pivot,-1):
            if nums[i]>nums[pivot]:
                next_value=i
                break
        nums[pivot],nums[next_value] =nums[next_value], nums[pivot]
        left,right=pivot+1,len(nums)-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        return nums