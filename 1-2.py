def checkPermutation(s1, s2):
    # early stopping
    if not len(s1) == len(s2): return False

    chars = {}
    for char in s1:
        chars[char] = chars.get(char,0) + 1
    for char in s2:
        chars[char] = chars.get(char,0) - 1
        # if chars[char] == 0:
        #     del chars[char]
    if set(chars.values()) == set([0]): return True
    else: return False

def check():
    print "This is 1-2 check string permutaion. Pls type 2 strings:"
    s1 = raw_input("string1 >> ")
    s2 = raw_input("string2 >> ")
    print checkPermutation(s1, s2)

if __name__ == "__main__":
    check()
