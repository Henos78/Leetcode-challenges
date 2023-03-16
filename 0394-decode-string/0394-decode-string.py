class Solution:
    def decodeString(self, s: str) -> str:
        
        def solve(i):
            res = ""
            num = 0
            
            while i < len(s):
                a = s[i]
                if a.isdigit():
                    num = num * 10 + int(a)
                elif a == '[':
                    string, end = solve(i + 1)
                    res += num * string
                    i = end
                    num = 0
                elif a == ']':
                    return res, i
                else:
                    res += a
                i += 1
            
            return res, i
        
        return solve(0)[0]
    
        # Remarks for self: Do it again while practicing all over again.