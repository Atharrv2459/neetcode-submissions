class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        m_marker = []
        n_marker = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    m_marker.append(i)
                    n_marker.append(j)
        for row in m_marker:
            for i in range(n):
                matrix[row][i] = 0
        for col in n_marker:
            for j in range(m):
                matrix[j][col] = 0
        
        