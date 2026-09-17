class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums)-1
        if(len(nums)==1):  return nums[0]
        if(nums[low]<nums[high]):   return nums[0]
        while(low<high):
            mid = (low+high)//2
            if(nums[low] < nums[mid] and nums[mid] > nums[high]):
                low = mid
            else:
                high = mid
        # print(mid)
        return nums[high+1]