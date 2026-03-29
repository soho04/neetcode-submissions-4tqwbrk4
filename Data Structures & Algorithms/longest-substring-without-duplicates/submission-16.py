class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0

        char_set = set()
        n = len(s)
        l = 0
        greatest = 0

        for r in range(n):

            if s[r] not in char_set:
                char_set.add(s[r])
                print("added ", s[r], char_set)
                greatest = max(r-l+1, greatest)
            
            else:

                while s[r] in char_set:
                    char_set.remove(s[l])
                    l += 1
                char_set.add(s[r])

                

        return greatest
        
        # zxyzxyz

        # pwwkew
        #             l   r
        # char_set = [p w w]