class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        ap = 0
        bp = 0
        
        result = []
        
        while (ap != len(A) and bp != len(B)):
            [a1, a2] = A[ap]
            [b1, b2] = B[bp]
            
            # A in B
            if a1 <= b1 and a2 >= b2:
                result.append([b1, b2])
                bp += 1
            # B in A
            elif a1 >= b1 and a2 <= b2:
                result.append([a1, a2])
                ap += 1
            elif a2 < b1:
                ap += 1
            elif b2 < a1:
                bp += 1
            else:
                result.append([max(a1, b1), min(a2, b2)])
                if a2 < b2:
                    ap += 1
                else:
                    bp += 1
            
        return result
