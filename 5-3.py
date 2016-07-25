def flipBitToWin(num):
    """
    One pass solution
    O(1) space
    """
    seq = "".join(bin(num).split("b"))
    prev, curr = 0, 0
    max_len = 1
    for i in range(len(seq)):
        char = seq[i]
        if char == "1":
            curr += 1
        elif char == "0": # == "0"
            prev = curr
            curr = 0
        if prev + curr + 1 > max_len:
            max_len = prev + curr + 1
    return max_len

def solution():
    print "5-3 filp to win. Pls enter a integer:"
    num = int(raw_input("integer >> "))
    print flipBitToWin(num)

if __name__ == "__main__":
    solution()
