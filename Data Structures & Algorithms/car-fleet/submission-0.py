class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort()
        res = []
        for i in range(len(cars)):
            while res and ((target - cars[i][0]) / cars[i][1] >= (target - res[-1][0]) / res[-1][1]):
                res.pop()
            res.append(cars[i])

        return len(res)