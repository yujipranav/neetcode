class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # brute force
        # res = 0
        # n = len(s)

        # for i in range(n):
        #     count, maxf = {}, 0
        #     for j in range(i, n):
        #         count[s[j]] = 1 + count.get(s[j],0)
        #         maxf = max(maxf, count[s[j]])
        #         if (j - i + 1) - maxf <= k:
        #             res = max(res, j - i + 1)

        # return res

        # sliding window
        # n = len(s)
        # res = 0
        # charSet = set(s)

        # for c in charSet:
        #     count = l = 0
        #     for r in range(n):
        #         if s[r] == c:
        #             count += 1
        #         while (r - l + 1) - count > k:
        #             if s[l] == c:
        #                 count -= 1
        #             l += 1

        #         res = max(res, r - l + 1)

        # return res 

        # sliding window optimized
        n = len(s)
        count = {}
        l = 0
        maxf = 0
        res = 0

        for r in range(n):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

        



