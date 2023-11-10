class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        i = 0

        while i < len(formula):
            if formula[i] == "(":
                stack.append("(")
                i += 1

            elif formula[i] == ")":
                i += 1
                count = ""
                while i < len(formula) and formula[i].isdigit():
                    count += formula[i]
                    i += 1
                count = int(count) if len(count) > 0 else 1

                j = len(stack) - 1
                while stack[j] != "(":
                    stack[j][1] *= count
                    j -= 1
                stack.pop(j)

            else:
                element = formula[i]
                i += 1
                while i < len(formula) and  formula[i].islower():
                    element += formula[i]
                    i += 1
                    
                count = ""
                while i < len(formula) and formula[i].isdigit():
                    count += formula[i]
                    i += 1
                count = int(count) if len(count) > 0 else 1
                stack.append([element, count])

        ans = ""
        stack.sort()
        i = 0
        
        while i < len(stack):
            totCount = stack[i][1]
            i += 1
            while i < len(stack) and stack[i][0] == stack[i-1][0]:
                totCount += stack[i][1]
                i += 1
            
            ans += (stack[i-1][0] + (str(totCount) if totCount > 1 else ""))
        
        return ans
            

            
            


        