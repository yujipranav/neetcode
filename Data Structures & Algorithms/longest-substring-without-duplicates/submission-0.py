class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0 
        
        # Brute force
        for i in range(n):
            charSet = set()
            for j in range(i,n):
                if s[j] in charSet:
                    break
                charSet.add(s[j])

            res = max(res, len(charSet))

        return res

        # Sliding window
        