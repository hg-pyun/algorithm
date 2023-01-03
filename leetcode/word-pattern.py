class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        pattern_list = []
        pattern_dup = {}

        for p in pattern:
            if p not in pattern_dup:
                pattern_list.append(p)
                pattern_dup[p] = 1

        mapper = {}
        dup = {}
        s_list = s.split()

        for word in s_list:
            if len(pattern_list) == 0:
                break
                
            if word not in dup:
                mapper[word] = pattern_list.pop(0)
                dup[word] = 1

        replaced_s = ''

        for word in s_list:
            if word in mapper:
                replaced_s += mapper[word]

        return pattern == replaced_s
