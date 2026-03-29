class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        l = 0
        frequency_map = defaultdict(int)
        greatest = 0
        highest_freq = 0

        for r in range(n):
            
            frequency_map[s[r]] += 1
            highest_freq = max(highest_freq, frequency_map[s[r]])

            while r-l+1 - highest_freq > k:
                frequency_map[s[l]] -= 1
                print("shrinking ", s[l])
                l += 1

            greatest = max(greatest, r-l+1)
            print(greatest, r, l)

        return greatest


            
            

        # l    r
        # AAABABB