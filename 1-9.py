def stringRotation(s1, s2):
    if not len(s1) == len(s2): return False
    s2_cat = s2+s2
    return isSubString(s2_cat, s1)

# Didn't get tested
