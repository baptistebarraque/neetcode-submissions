class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        P=1
        number_of_zeroes=0
        for i in range(len(nums)):
            if nums[i]==0:
                number_of_zeroes+=1
                if number_of_zeroes > 1:
                    return [0 for i in range(len(nums))]
            else:
                P*=nums[i]
        L=[]
        for i in range(len(nums)):
            if nums[i]==0:
                L.append(P)
            else:
                if number_of_zeroes > 0:
                    L.append(0)
                else:
                    L.append(P//nums[i])
        return L

            
        