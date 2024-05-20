class Solution:
    def checkObstacles(self, x, y, obstacles):
        return (x, y) in obstacles

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x = 0
        y = 0
        # n, s, e, w
        d = 'n'
        ans = 0

        obstacle_set = set(map(tuple, obstacles))

        for cmd in commands:
            if cmd == -2:
                if d == 'n':
                    d = 'w'
                elif d == 's':
                    d = 'e'
                elif d == 'e':
                    d = 'n'
                elif d == 'w':
                    d = 's'
            elif cmd == -1:
                if d == 'n':
                    d = 'e'
                elif d == 's':
                    d = 'w'
                elif d == 'e':
                    d = 's'
                elif d == 'w':
                    d = 'n'
            else:
                if d == 'n':
                    for i in range(cmd):
                        if self.checkObstacles(x, y + 1, obstacle_set):
                            break
                        y += 1
                elif d == 's':
                    for i in range(cmd):
                        if self.checkObstacles(x, y - 1, obstacle_set):
                            break
                        y -= 1
                elif d == 'e':
                    for i in range(cmd):
                        if self.checkObstacles(x + 1, y, obstacle_set):
                            break
                        x += 1
                elif d == 'w':
                    for i in range(cmd):
                        if self.checkObstacles(x - 1, y, obstacle_set):
                            break
                        x -= 1

            dist = x * x + y * y
            if ans < dist:
                ans = dist

        return ans
