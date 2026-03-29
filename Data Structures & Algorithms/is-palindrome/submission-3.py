class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = re.sub(r'[^A-Za-z0-9]', '', s)
        
        clean_string = s.lower()

        print(clean_string)
        list(clean_string)

        return clean_string == clean_string[::-1]