class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = defaultdict(list)
        res = []

        for string in strs:
            anagram_map[str(sorted(string))].append(string)
            
        for array in anagram_map.values():
            res.append(array)

        return res
        
        
    





        