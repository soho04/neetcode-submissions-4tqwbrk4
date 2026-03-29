class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0

        l = 0
        nums_set = set()
        count = 0
        greatest = 0

        for i in range(len(s)):

            # print(s[i])

            if s[i] not in nums_set:
                nums_set.add(s[i])
                count += 1
                greatest = max(greatest, count)

            else:
                while s[i] in nums_set:
                    print(s[l])
                    nums_set.remove(s[l])
                    l += 1
                print("finished at ", s[l], " at index ", l)
                nums_set.add(s[i])
                count = i - l +1

        return greatest

        # l 
        # i
        # dvdf