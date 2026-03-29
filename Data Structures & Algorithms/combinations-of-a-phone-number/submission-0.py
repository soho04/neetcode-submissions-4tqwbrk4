class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []

        res = []

        keypad = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}


        def backtrack(curr, start):

            if len(curr) >= len(digits):
                res.append(curr[:])
                return

            for letter in keypad[digits[start]]:
                backtrack(curr+letter, start+1)

        backtrack("", 0)

        return res
                

        # 23

        # 2: a, b, c 3: d, e, f

        # ad, ae, af, bd

            
