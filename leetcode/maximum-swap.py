class Solution:
    def maximumSwap(self, num: int) -> int:

        splited = list(str(num))
        sorted_splited = sorted(list(str(num)), reverse=True)


        target_index = -1

        for i in range(len(splited)):
            if splited[i] != sorted_splited[i]:
                target_index = i
                break

        if target_index == -1:
            return num
        
        max_num = '0'
        max_index = target_index

        for i in range(len(splited) - 1, target_index, -1):
            if splited[i] > max_num:
                max_num = splited[i]
                max_index = i
        
        splited[target_index], splited[max_index] = splited[max_index], splited[target_index]

        ans = ''

        for s in splited:
            ans += s
        
        return int(ans)
