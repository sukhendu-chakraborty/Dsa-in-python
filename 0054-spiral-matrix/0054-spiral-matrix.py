class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        total = m * n
        ans = []
        c = 0
        
        # Start at row 0 and column 0
        row = 0
        col = 0
        
        while c < total:
            # 1. First row direction (Left to Right)
            for j in range(col, m):
                if c == total: break
                ans.append(matrix[row][j])
                c += 1
            row += 1  # Move the top boundary down by 1 row
            
            # 2. Last column direction (Top to Bottom)
            for i in range(row, n):
                if c == total: break
                ans.append(matrix[i][m - 1])
                c += 1
            m -= 1  # Shrink the right column boundary inward
            
            # 3. Last row direction (Right to Left)
            for j in range(m - 1, col - 1, -1):
                if c == total: break
                ans.append(matrix[n - 1][j])
                c += 1
            n -= 1  # Shrink the bottom row boundary upward
            
            # 4. First column direction (Bottom to Top)
            for i in range(n - 1, row - 1, -1):
                if c == total: break
                ans.append(matrix[i][col])
                c += 1
            col += 1  # Move the left column boundary inward
            
        return ans
