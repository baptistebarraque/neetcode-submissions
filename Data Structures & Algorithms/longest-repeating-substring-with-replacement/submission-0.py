
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)   # fréquences dans la fenêtre courante
        left = 0
        max_freq = 0               # plus grande fréquence vue dans une fenêtre
        best = 0
        for right, c in enumerate(s):
            count[c] += 1
            max_freq = max(max_freq, count[c])
            # trop de caractères à remplacer : on rétrécit par la gauche
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
                
                



