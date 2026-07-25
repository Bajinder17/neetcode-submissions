class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        low, high = 0, n*m-1

        while low <= high:
            guess = (low+high)//2
            row = guess // m
            col = guess % m

            if matrix[row][col] ==  target:
                return True
            elif matrix[row][col] < target:
                low = guess + 1
            else:
                high = guess - 1
        
        return False
