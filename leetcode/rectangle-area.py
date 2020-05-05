class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area1 = abs(C - A) * abs(D - B)
        area2 = abs(G - E) * abs(H - F)
        overlap = max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)
        
        return area1 + area2 - overlap
