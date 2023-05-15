#Rotate Image by 90 - Brute Force


class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        #creating a dummy matrix by getting 0 0 0 then for the range of n - meaning 3 more times
        dummy = [[0]*n for i in range(n)]
        

        for r in range(n):
            for c in range(n):
                dummy[c][n-r-1] = matrix[r][c]

        for r in range(n):
            for c in range(n):
                matrix[r][c] =dummy[r][c]

