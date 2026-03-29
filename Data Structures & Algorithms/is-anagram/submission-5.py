class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        map1, map2 = defaultdict(int), defaultdict(int)

        for char in s:
            map1[char] += 1 + map1.get(map1[char], 0)

        for char in t:
            map2[char] += 1 + map2.get(map2[char], 0)

        return map1 == map2