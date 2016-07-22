def rotateMatrix(Matrix, N):
    if N == 1: return Matrix
    if N % 2 == 0: n = m = N / 2
    else:
        n = N / 2
        m = N - n
    
    print "Before: "
    reprMatrix(Matrix, N)

    for i in range(0, n):
        for j in range(0, m):
            Matrix[i][j], Matrix[j][N-1-i], Matrix[N-1-i][N-1-j], Matrix[N-1-j][i] = Matrix[N-1-j][i], Matrix[i][j], Matrix[j][N-1-i], Matrix[N-1-i][N-1-j]

    print "After: "
    reprMatrix(Matrix, N)

def reprMatrix(Matrix, N):
    for i in range(0, N):
        print Matrix[i]

def solution():
    print "1-7 rotate matrix, Using default matrix."
    M1 = [[1,2,3],[4,5,6],[7,8,9]]
    M2 = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
    rotateMatrix(M1, 3)
    rotateMatrix(M2, 4)

if __name__ == "__main__":
    solution()
