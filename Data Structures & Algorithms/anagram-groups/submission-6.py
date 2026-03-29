class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = defaultdict(list[str])

        # for string in strs:
        #     key = ''.join(sorted(string))
        #     anagram_map[key].append(string)

        for string in strs:
            key = [0] * 26
            for c in string:
                key[ord(c) - ord('a')] += 1

            key_tuple = tuple(key)
            anagram_map[key_tuple].append(string)

        return list(anagram_map.values())

    