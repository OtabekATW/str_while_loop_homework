def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    k = 0
    lower = ''
    while i < len(s):
        if s[i].islower():
            #lower += s[i]
            k += 1
        i += 1
    return k #len(lower) 