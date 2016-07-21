def oneAway(s1, s2):
    if abs(len(s1) - len(s2)) > 1: return False
    l1 = list(s1)
    l2 = list(s2)
    popSame(l1, l2, 0)
    popSame(l1, l2, -1)
    if (len(l1)==1 or len(l2)==1) and len(l1)+len(l2)<=2:
        return True
    else: 
        return False

def popSame(l1, l2, idx):
    while l1 and l2:  # no empty list
        if l1[idx] == l2[idx]:
            l1.pop(idx)
            l2.pop(idx)
        else:
            break

def check():
    print "1-5 One way, pls enter two strings."
    s1 = raw_input("string1 >> ")
    s2 = raw_input("string2 >> ")
    print oneAway(s1, s2)

if __name__ == "__main__":
    check()
