class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()

        left, right = 0, 0
        greatest = 0

        while right < len(s):
            
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            if s[right] not in charSet:
                charSet.add(s[right])

            greatest = max(greatest, len(charSet))
            right += 1

        return greatest

