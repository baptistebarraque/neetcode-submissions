class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        left = 0
        max_size = 0
        for right, c in enumerate(s):
            if c in last_index and last_index[c] >= left:
                left = last_index[c] + 1
            last_index[c] = right
            max_size = max(max_size, right - left + 1)
        return max_size

        