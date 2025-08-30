class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)

        def rotations(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        rotations(0,len(nums)-1)
        rotations(0,k-1)
        rotations(k,len(nums)-1)
