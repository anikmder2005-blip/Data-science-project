class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        datesOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefixSum = [0]
        for date in datesOfMonths:
            prefixSum.append(prefixSum[-1] + date)

        arriveAliceDay = self.calculatedayOfYear(arriveAlice, prefixSum)
        leaveAliceDay = self.calculatedayOfYear(leaveAlice, prefixSum)
        arriveBobDay = self.calculatedayOfYear(arriveBob, prefixSum)
        leaveBobDay = self.calculatedayOfYear(leaveBob, prefixSum)
        return max(
            0,
            min(leaveAliceDay, leaveBobDay)
            - max(arriveAliceDay, arriveBobDay)
            + 1
        )

    def calculatedayOfYear(self, day: str, prefixSum: List[int]) -> int:
        month = int(day[:2])
        date = int(day[3:])
        return prefixSum[month - 1] + date