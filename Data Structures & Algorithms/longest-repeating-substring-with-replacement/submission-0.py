class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # increment the count of the current char found
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k: # if the number of replacements is larger than the num allowed in k, make the window smaller
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1) # update result to the largest size of the window
        return res