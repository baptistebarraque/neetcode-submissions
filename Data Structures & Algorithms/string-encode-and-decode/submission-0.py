class Solution:

    def __init__(self):
        self.size_dict={}

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in range(len(strs)):
            self.size_dict[i]=len(strs[i])
            s+=strs[i]
       
        return s



    def decode(self, s: str) -> List[str]:
        strs=[]
        k=0
        
        for i in sorted(self.size_dict.keys()):
            s_chunk=""
            for j in range(self.size_dict[i]):
                s_chunk+=s[k]
                k+=1
            strs.append(s_chunk)
                
        return strs

