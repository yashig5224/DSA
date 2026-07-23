class Solution(object):

    def canCompleteCircuit(self, gas, cost):

        totalGas = 0
        totalCost = 0

        currentGas = 0
        start = 0

        for i in range(len(gas)):

            totalGas += gas[i]
            totalCost += cost[i]

            currentGas += gas[i] - cost[i]

            # Current starting point is invalid
            if currentGas < 0:
                start = i + 1
                currentGas = 0

        # Total fuel is insufficient
        if totalGas < totalCost:
            return -1

        return start