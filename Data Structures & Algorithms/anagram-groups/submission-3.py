class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        array_maps = {}
        final_list = []

        for st in strs:
            key = ''.join(sorted(st))
            if key in array_maps:
                array_maps[key].append(st)
            else:
                array_maps[key] = [st]

        for arrays in array_maps.values():
            final_list.append(arrays)

        return final_list
