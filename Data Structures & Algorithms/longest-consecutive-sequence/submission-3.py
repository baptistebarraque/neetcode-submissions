class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums_set=set(nums)
        
        max=1
        for i in range(len(nums)):
            if nums[i]-1 not in nums_set:
                k=1
                while nums[i]+k in nums_set:
                    k+=1
                else:
                    if max<k:
                        max=k
        return max



        