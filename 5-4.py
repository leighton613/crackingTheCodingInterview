def nextNumber(num):
    print "the number is ", num, bin(num)
    strNum = "".join(bin(num).split('b'))
    nextSmallest = list(strNum)
    nextLargest = list(strNum)
    winS = ["1","0"]
    winL = ["0","1"]
    for i in range(len(strNum)-1, 0, -1):

        win = nextSmallest[i-1:i+1]
        if win == winS:
            nextSmallest[i], nextSmallest[i-1] = nextSmallest[i-1], nextSmallest[i]
            print "the smallest next ", "".join(nextSmallest)
            numS = int("".join(nextSmallest), 2)
            break
    else:
        print "smallest next NOT FOUND"
        numS = None

    for i in range(len(strNum)-1, 0, -1):
        win = nextLargest[i-1:i+1]
        if win == winL:
            nextLargest[i], nextLargest[i-1] = nextLargest[i-1], nextLargest[i]
            print "the largest next ", "".join(nextLargest)
            numL = int("".join(nextLargest), 2)
            break
    else:
        print "largest next NOT FOUND"
        numL = None
    return numS, numL

def solution():
    print "5-4 next number. Pls enter a positive integer."
    num = int(raw_input("pos. int >> "))
    numS, numL = nextNumber(num)
    print numS, numL

if __name__ == "__main__":
    solution()
