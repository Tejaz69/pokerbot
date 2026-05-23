def solve_psne(p1_matrix, p2_matrix):
    n = len(p1_matrix)
    m = len(p1_matrix[0])
    psne = []
    for i in range(n):
        for j in range(m):
            max_p1 = max(p1_matrix[r][j] for r in range(n))
            max_p2 = max(p2_matrix[i][c] for c in range(m))
            if p1_matrix[i][j] == max_p1 and p2_matrix[i][j] == max_p2:
                psne.append((i, j))
    return psne
