class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        nrow, ncol = len(matrix), len(matrix[0])
        l_wall, r_wall = -1, ncol
        u_wall, d_wall = 0, nrow
        direction = 'r'
        result = []
        i, j = 0, 0
        while len(result) < nrow * ncol:
            result.append(matrix[i][j])
            if direction == 'r':
                j += 1
                if j == r_wall:
                    r_wall -= 1
                    j = r_wall
                    direction = 'd'
                    i += 1
            elif direction == 'd':
                i += 1
                if i == d_wall:
                    d_wall -= 1
                    i = d_wall
                    direction = 'l'
                    j -= 1
            elif direction == 'l':
                j -= 1
                if j == l_wall:
                    l_wall += 1
                    j = l_wall
                    direction = 'u'
                    i -= 1
            elif direction == 'u':
                i -= 1
                if i == u_wall:
                    u_wall += 1
                    i = u_wall
                    direction = 'r'
                    j += 1
        return result
