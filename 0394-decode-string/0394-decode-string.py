class Solution:
    def decodeString(self, s: str) -> str:
        result = ""
        stack = []
        
        for ch in s:
            if ch == "]":
                temp = ""
                while stack[-1] != "[":
                    temp = stack.pop() + temp
                    
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                k = int(k)
                
                wordAfterRepeatition = temp
                while k > 1:
                    wordAfterRepeatition += temp
                    k -= 1
                    
                if stack:
                    stack.append(wordAfterRepeatition)  
                else:
                    result += wordAfterRepeatition
            
            else:
                stack.append(ch)
                
        if stack:
            result += "".join(stack)
                
        return result if not result.isdigit() else ""
            
            
        
        