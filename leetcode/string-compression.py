class Solution:
    def compress(self, chars: List[str]) -> int:
        box = None
        c = 0
        length = len(chars)
        flatten = lambda t: [item for sublist in t for item in sublist]
        
        for i in range(length):
            if box is None:
                box = chars[i]
            elif chars[i] != chars[i - 1]:
                chars.append(box)
                if c != 1:
                    for char in list(str(c)):
                        chars.append(char)
                box = chars[i]
                c = 0
            
            if i == length - 1:
                chars.append(box)
                if c != 0:
                    for char in list(str(c + 1)):
                        chars.append(char)
            
            c += 1
    
        for i in range(length):
            chars.pop(0)
        
        return len(chars)
