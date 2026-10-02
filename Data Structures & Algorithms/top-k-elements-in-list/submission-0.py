class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        frequencies=[]
        for key in d:
            frequencies.append((d[key], key))
        frequencies=sorted(frequencies, reverse=True)
        l=[]
        for e in frequencies[:k]:
            l.append(e[1])
        return l

        