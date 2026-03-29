class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        code_s, code_t = [0] * 26, [0] * 26

        for char in s:
            code_s[ord(char) - ord('a')] += 1

        for char in t:
            code_t[ord(char) - ord('a')] += 1

        return code_s == code_t

        # Time complexity: O(n + m) 
        # Because we traverse both s and t
        # Space complexity: O(1)
        # Despite the frequency, we have a fixed set of characters we can choose from - the alphabet
