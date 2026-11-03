class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if not stack or asteroid > 0:
                stack.append(asteroid)
            else:
                add = True
                while stack and stack[-1] > 0:
                    if stack[-1] < abs(asteroid):
                        stack.pop()
                    elif stack[-1] == abs(asteroid):
                        stack.pop()
                        add = False
                        break
                    else:
                        add = False
                        break
                if add:
                    stack.append(asteroid)

        return stack