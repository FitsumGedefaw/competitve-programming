class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            stack.append(asteroid)

            while len(stack) >= 2 and stack[-1] < 0 and stack[-2] > 0:
                topAst = stack.pop()
                bottomAst = stack.pop()
                if abs(topAst) < bottomAst:
                    stack.append(bottomAst)
                elif abs(topAst) > bottomAst:
                    stack.append(topAst)

        return stack
                    


        