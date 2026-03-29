class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l, sizeofs1 = 0, len(s1)

        while l < len(s2) - len(s1)+1:

            print(s2[l:l+sizeofs1])
            
            if sorted(s2[l:l+sizeofs1]) == sorted(s1):
                return True

            l += 1

        return False



            