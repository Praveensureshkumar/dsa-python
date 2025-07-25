class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        row_zero = False
        col_zero = False

        # Step 1: Check if first row or first column have any zeros
        for i in range(row):
            if matrix[i][0] == 0:
                col_zero = True
        for j in range(col):
            if matrix[0][j] == 0:
                row_zero = True

        # Step 2: Use rest of matrix as markers
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 3: Set zeros based on markers
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 4: Zero first row if needed
        if row_zero:
            for j in range(col):
                matrix[0][j] = 0

        # Step 5: Zero first column if needed
        if col_zero:
            for i in range(row):
                matrix[i][0] = 0
                
