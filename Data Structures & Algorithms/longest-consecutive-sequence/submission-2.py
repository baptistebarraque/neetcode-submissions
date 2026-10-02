class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums_set=set(nums)
        start_of_sequence_idx=[]
        for i in range(len(nums)):
            if nums[i]-1 not in nums_set:
                start_of_sequence_idx.append(i)
        
        max=1
        for i in start_of_sequence_idx:
            k=1
            print(nums[i]+k)
            while nums[i]+k in nums_set:
                k+=1
            else:
                if max<k:
                    max=k
        return max



        