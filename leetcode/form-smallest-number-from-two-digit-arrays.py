class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        
        MAX_NUM = 10

        checker = [False for _ in range(MAX_NUM)]
        lowest_dup_num = MAX_NUM
        lowest_num1 = MAX_NUM
        lowest_num2 = MAX_NUM

        for num in nums1:
            checker[num] = True
            lowest_num1 = min(lowest_num1, num)

        for num in nums2:
            if checker[num]:
                print('c', num)
                lowest_dup_num = min(lowest_dup_num, num)
            lowest_num2 = min(lowest_num2, num)
        
        if lowest_dup_num != MAX_NUM:
            return lowest_dup_num
        else:
            if lowest_num1 > lowest_num2:
                return int(str(lowest_num2) + str(lowest_num1))
            else:
                return int(str(lowest_num1) + str(lowest_num2))
