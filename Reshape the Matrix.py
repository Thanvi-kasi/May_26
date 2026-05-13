class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        # If reshape is not possible, return original matrix
        if m * n != r * c:
            return mat

        # Create reshaped matrix
        result = [[0] * c for _ in range(r)]

        for i in range(m * n):
            result[i // c][i % c] = mat[i // n][i % n]

        return result
