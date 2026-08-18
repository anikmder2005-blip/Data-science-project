class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = rows*cols - 1
        while l<=r:
            mid = (l+r)//2

            i = mid//cols
            j = mid%cols

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                #left
                r = mid-1
            else:
                # right
                l =mid+1

        return False