class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        stack=[]
        openings=['{','[','(']
        closings=[']','}',')']
        match={']':'[','}':'{',')':'('}
        for i in range(len(s)):
            if s[i] in openings:
                stack.append(s[i])
            if s[i] in closings:
                if len(stack)==0:
                    return False
                e=stack.pop()
                if e!=match[s[i]]:
                    return False
        if len(stack)>0:
            return False
        return True


        