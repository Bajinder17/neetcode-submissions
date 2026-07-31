class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        res,low,maxi = 0,0,0

        for high in range(len(s)):
            freq[s[high]] = freq.get(s[high], 0) + 1
            maxi = max(maxi, freq[s[high]])

            while(high-low+1) - maxi > k:
                freq[s[low]] -= 1
                low += 1
            res = max(res, high-low+1)
        return res