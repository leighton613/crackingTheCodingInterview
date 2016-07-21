def stringCompression(s):
    if len(s) <= 2: return s
    list_comp = [s[0], 1]
    for i in range(1, len(s)):
        char = s[i]
        if char == list_comp[-2]:
            list_comp[-1] += 1
        else:
            list_comp.append(char)
            list_comp.append(1)
    s_comp = "".join([str(i) for i in list_comp])
    if len(s) <= len(s_comp):
        return s
    else: 
        return s_comp

def solution():
    print "1-6 string compression. Pls enter a string."
    s = raw_input("string >>")
    print stringCompression(s)

if __name__ == "__main__":
    solution()
