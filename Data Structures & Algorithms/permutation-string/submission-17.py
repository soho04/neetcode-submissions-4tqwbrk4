class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False        

        i = len(s1)
        coded_s1 = [0] * 26
        window = [0] * 26
        l = 0

        for char in range(len(s1)):
            coded_s1[ord(s1[char])- ord('a')] += 1
            window[ord(s2[char])-ord('a')] += 1

        if window == coded_s1:
            return True

        for r in range(i, len(s2)):

            window[ord(s2[l]) - ord('a')] -= 1
            window[ord(s2[r]) - ord('a')] += 1
            l += 1

            if window == coded_s1:
                return True

        return False

