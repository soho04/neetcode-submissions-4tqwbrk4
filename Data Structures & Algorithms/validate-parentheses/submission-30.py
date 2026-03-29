class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        char_map = {"]": "[", ")": "(", "}": "{"}

        for char in s:

            if char in "([{":
                stack.append(char)

            elif stack and stack[-1] == char_map[char]:
                stack.pop()

            else:
                return False

        return len(stack) == 0



    # "([{}])"

    # "[(])"