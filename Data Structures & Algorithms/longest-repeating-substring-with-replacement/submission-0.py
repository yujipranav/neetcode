class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # brute force
        res = 0
        n = len(s)

        for i in range(n):
            count, maxf = {}, 0
            for j in range(i, n):
                count[s[j]] = 1 + count.get(s[j],0)
                maxf = max(maxf, count[s[j]])
                if (j - i + 1) - maxf <= k:
                    res = max(res, j - i + 1)

        return res