def insertion(M, N, i, j):
    """
    space btwn i and j is guaranteed to be large enough for M;
    assume that the extra space remains N's content
    """
    i = j - len(M) + 1
    mask = ((1 << i) - 1) | (-1 << (j + 1))
    return (N & mask) | (M << i)
