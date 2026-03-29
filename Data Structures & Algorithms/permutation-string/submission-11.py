class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l, r = 0, len(s1)-1

        s1_code = [0] * 26
        for char in s1:
            index = ord(char) - ord('a')
            s1_code[index] += 1

        while r < len(s2):

            string_code = [0] * 26

            for char in s2[l:r+1]:
                index = ord(char) - ord('a') 
                string_code[index] += 1
            
            if string_code == s1_code:
                return True
            
            r += 1
            l += 1  

        return False

