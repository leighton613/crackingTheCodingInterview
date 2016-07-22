def reprMatrix(Matrix, N):
    for i in range(0, N):
        print Matrix[i]

def zeroMatrix(Matrix, M, N):
    rowFlag = [0 for i in range(M)]
    colFlag = [0 for j in range(N)]
    for i in range(M):
        for j in range(N):
            if Matrix[i][j] == 0:
                rowFlag[i] = 1
                colFlag[j] = 1

    for i in range(M):
        for j in range(N):
            if rowFlag[i] == 1 or colFlag[j] == 1:
                Matrix[i][j] = 0

    reprMatrix(Matrix, M)

def zeroMatrix2(Matrix, M, N):
    rowHasZero, colHasZero = 0, 0
    for i in range(M):
        if Matrix[i][0] == 0:
            colHasZero = 1
            break
    for j in range(N):
        if Matrix[0][j] == 0:
            rowHasZero = 1
            break

    for i in range(1,M):
        for j in range(1,N):
            if Matrix[i][j] == 0:
                Matrix[i][0] = 0
                Matrix[0][j] = 0
    for i in range(1,M):
        for j in range(1,N):
            if Matrix[i][0] == 0 or Matrix[0][j] == 0:
                Matrix[i][j] = 0

    if colHasZero == 1:
        for i in range(M):
            Matrix[i][0] = 0
    if rowHasZero == 1:
        for j in range(N):
            Matrix[0][j] = 0

    reprMatrix(Matrix, M)

def solution():
    """
    O(M+N) space
    O(MN) time
    """
    print "1-8 Zero matrix. Using defalt matrix."
    M = [[1,2,3],[4,5,6],[7,0,9]]
    zeroMatrix(M, 3, 3)

def solution2():
    """
    O(1) space
    O(MN) time
    """
    print "1-8 Zero matrix (sol 2). Using defalt matrix."
    M = [[1,2,3],[4,5,6],[7,0,9]]
    zeroMatrix2(M, 3, 3)

if __name__ == "__main__":
    solution2()
