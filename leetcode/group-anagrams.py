class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = []
        for str in strs:
            count.append(''.join(sorted(str)))

        map = {}
        for i in range(len(count)):
            if map.get(count[i]) is None:
                map[count[i]] = [strs[i]]
            else:
                map[count[i]].append(strs[i])

        return list(map.values())
