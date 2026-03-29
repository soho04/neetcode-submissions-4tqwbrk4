class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = "" # Empty result string to store the encoded strings
        for s in strs:
            res += str(len(s)) + "#" + s # For each string, append length followed by '#' and the string itself
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 # Empty list and initialised pointer to traverse encoded string

        while i < len(s): # Loop until end of encoded string
            j = i # Set pointer 'j' which will find the position of the delimiter '#'
            while s[j] != "#": # Move 'j' to find '#' the separates length of string from actual string
                j += 1 # Increment 'j' into; # is found
            length = int(s[i:j]) # Extract length of next string
            res.append(s[j + 1 : j + 1 + length]) # Add the string to the result list strating after '#' and extracting 'length' characters
            i = j + 1 + length # Move index 'i' to the position after the current string, past the ewxtracted string
        return res
