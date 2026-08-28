class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
        matrix[:] = [row[::-1] for row in m]