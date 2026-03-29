class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""

        for s in strs:
            string += str(len(s)) + "#" + s

        return string


    def decode(self, s: str) -> List[str]:
        
        i, j = 0, 0

        strings = []

        print(s)

        while i < len(s):

            if s[i] == '#':
                length = s[j:i]
                j = i + 1
                i += int(length)
                strings.append(s[j:i+1])
                j = i + 1
            
            i += 1


        return strings


        