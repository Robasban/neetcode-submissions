class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        check = 0
        tank = 0
        while check < len(gas):
            tank = 0
            i = check
            while tank >= 0:
                tank += gas[i]
                tank -= cost[i]
                i += 1
                if i == len(gas):
                    i = 0
                if tank < 0:
                    if i <= check:
                        return -1
                    check = i
                elif i == check:
                    return check
        return -1