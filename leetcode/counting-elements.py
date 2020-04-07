class Solution:
    def countElements(self, arr: List[int]) -> int:
        map = {}
        for n in arr:
            if map.get(n) is None:
                map[n] = 1
            else:
                map[n] += 1

        count = 0
        for key in map.keys():
            count += map.get(key + 1) is not None and map.get(key)

        return count
