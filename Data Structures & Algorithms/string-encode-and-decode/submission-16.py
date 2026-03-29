class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""

        for string in strs:
            encoded_string += str(len(string)) + "#" + string

        return encoded_string


    def decode(self, s: str) -> List[str]:

        i = 0
        res = []

        print(s)
        
        while i < len(s):

            j = i

            word_length = ""
            
            while s[j] != "#":
                word_length += s[j]
                j += 1
            
            x = int(word_length)
            wordStart = j+1
            wordEnd = wordStart + x

            word = s[wordStart : wordEnd]

            res.append(word)
        
            i = wordEnd

        return res

    #             j
    #             i 
    # 4#neet4#code4#love3#you

