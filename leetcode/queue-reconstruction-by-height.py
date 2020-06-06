class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key = itemgetter(1))
        people = sorted(people, key = itemgetter(0), reverse = True)
        
        res = []
        for p in people:
            res.insert(p[1], p)
            
        return res
