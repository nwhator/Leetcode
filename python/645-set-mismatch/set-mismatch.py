class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        totalSum = sum(nums)
        # Expected sum of first n natural numbers
        expectedSum = n * (n + 1) // 2
        # Sum o squares of the numbers in an array
        squareSum = sum(x ** 2 for x in nums)
        # Expected sum of squares of first n natural numbers
        expectedSquareSum = n * (n + 1) * (2 * n + 1) // 6
        missingNum = expectedSum - totalSum
        diffSquare = expectedSquareSum - squareSum
        # Duplicated number - Missing number
        dupMinusMissing = diffSquare // missingNum
        dupNum = (missingNum + dupMinusMissing) // 2
        missingNum = (dupMinusMissing - missingNum) // 2

        return [missingNum, dupNum]