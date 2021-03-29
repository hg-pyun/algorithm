class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop();
