class Solution:

    def encode(self, strs: List[str]) -> str:
        _str = ""

        for s in strs:
            _str += s+"4#"

        return _str


    def decode(self, s: str) -> List[str]:
        
        arr = s.split("4#")
        arr.pop()

        return arr