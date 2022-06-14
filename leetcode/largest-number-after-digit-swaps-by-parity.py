class Solution:
    def largestInteger(self, num: int) -> int:
        num_arr = list(map(int, list(str(num))))
        
        for i in range(len(num_arr)):
            candidate = num_arr[i] % 2
            max_num = num_arr[i]
            target_index = i
        
            for j in range(i, len(num_arr)):
                n = num_arr[j]
                if n % 2 == candidate and n > max_num:
                    target_index = j
                    max_num = n
                
            num_arr[i], num_arr[target_index] = num_arr[target_index], num_arr[i]
        
        return int(''.join(list(map(str, num_arr))))
