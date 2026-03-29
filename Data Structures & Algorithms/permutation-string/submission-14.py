class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        i = len(s1)-1
        coded_s1 = [0] * 26

        for char in s1:
            coded_s1[ord(char)- ord('a')] += 1

        for r in range(len(s1)-1, len(s2)):

            substr = s2[r-len(s1)+1:r+1]
            print(substr)
            code = [0] * 26

            for char in substr:
                code[ord(char) - ord('a')] += 1

            if code == coded_s1:
                return True

        return False

