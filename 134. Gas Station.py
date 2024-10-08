class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        slicer = 0
        sum = 0
        while slicer - start < len(gas):
            sum += gas[slicer] - cost[slicer]
            while slicer - start < len(gas) and sum < 0:
                start -= 1
                sum += gas[start] - cost[start]
            slicer += 1

        if sum >= 0:
            return start if start >= 0 else len(gas) + start
        return -1
