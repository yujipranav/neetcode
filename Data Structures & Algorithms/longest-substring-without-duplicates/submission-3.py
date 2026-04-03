class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0 
        
        # Brute force
        # for i in range(n):
        #     charSet = set()
        #     for j in range(i,n):
        #         if s[j] in charSet:
        #             break
        #         charSet.add(s[j])

        #     res = max(res, len(charSet))

        # return res

        # Sliding window
        l = 0
        charSet = set()
        
        for r in range(n):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res