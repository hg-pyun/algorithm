class Solution:
    def countTime(self, time: str) -> int:
        
        h1 = time[0]
        h2 = time[1]

        m1= time[3]
        m2= time[4]

        h_count = 1
        m_count = 1

        if h1 == '?' and h2 == '?':
            h_count = 24
        elif h1 == '?' and h2 != '?':
            if int(h2) >= 4:
                h_count = 2
            else:
                h_count = 3
        elif h1 != '?' and h2 == '?':
            if h1 == '0' or h1 == '1':
                h_count = 10
            else:
                h_count = 4

        if m1 == '?' and m2 == '?':
            m_count = 60
        elif m1 == '?' and m2 != '?':
            m_count = 6
        elif m1 != '?' and m2 == '?':
            m_count = 10

        return h_count * m_count
