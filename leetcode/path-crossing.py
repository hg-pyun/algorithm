class Solution:
    def isPathCrossing(self, path: str) -> bool:

        x = 0
        y = 0

        map = {
            "0.0": True
        }

        for str in path:
            if str == "N":
                y += 1
            elif str == "S":
                y -= 1
            elif str == "E":
                x -= 1
            elif str == "W":
                x += 1
            
            p = f'{x}.{y}'
            
            if p in map:
                return True
            
            map[p] = True

        return False
