class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        list_map = {}
        arr = []

        for s in strs:
            key = "".join(sorted(s))
            if not list_map.get(key):
                list_map[key] = [s]
            else:
                list_map[key].append(s)
        
        for x in list_map.keys():
            arr.append(list_map[x])

        return arr