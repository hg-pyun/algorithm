class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        
        group = 0
        l = len(colors)

        for i in range(0, l):
            prev_color = colors[(i - 1) % l]
            current_color = colors[i]
            next_color = colors[(i + 1) % l]

            if (prev_color == next_color) and prev_color != current_color:
                group += 1

        return group
      
