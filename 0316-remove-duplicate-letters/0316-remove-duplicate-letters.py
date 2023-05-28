class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = {}
        for ch in s:
            if ch not in dic:
                dic[ch] =1
            else:
                dic[ch] +=1

        stack = []
        seen = set()

        for ch in s:
            dic[ch] -= 1
            
            if ch in seen:
                continue
            while stack and stack[-1] > ch and dic[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(ch)
            seen.add(ch)

        return ''.join(stack)