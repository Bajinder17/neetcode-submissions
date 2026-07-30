class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        low, res = 0, 0
        freq = {}

        for high in range(n):
            freq[s[high]] = freq.get(s[high], 0) + 1

            while freq[s[high]] > 1:
                freq[s[low]] -= 1

                if freq[s[low]] == 0:
                    del freq[s[low]]
                low += 1
            
            res = max(res, high-low + 1)
        return res