class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False 
        d_s={}
        d_t={}
        for i in range(len(s)):
            if s[i] in d_s:
                d_s[s[i]]+=1
            else :
                d_s[s[i]]=0
            if t[i] in d_t:
                d_t[t[i]]+=1
            else :
                d_t[t[i]]=0
        for key in d_s:
            if key not in d_t:
                return False
            if d_s[key]!=d_t[key]:
                return False
        return True

        