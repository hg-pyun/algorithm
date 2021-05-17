class MyCalendar:

    def __init__(self):
        self.book_list = []
        

    def book(self, start: int, end: int) -> bool:
        for [bs, be] in self.book_list:
            if start < be and end > bs:
                return False
        
        self.book_list.append([start, end])
        
        return True
