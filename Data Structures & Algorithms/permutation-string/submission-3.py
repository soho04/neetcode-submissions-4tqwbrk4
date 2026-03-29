class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l, r = 0, len(s1) 

        # while r <= len(s2):
            
        #     if sorted(s2[l:r]) == sorted(s1):
        #         return True
            
        #     l += 1
        #     r += 1

        for r in range(r, len(s2)+1):

            print("stepping ", l, r, " with value ", s2[l:r])
            
            if sorted(s2[l:r]) == sorted(s1):
                return True

            l += 1

        return False

            