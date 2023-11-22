def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    k = 0
    upper = ''
    while i < len(s):
        if s[i].isupper():
            #upper += s[i]
            k += 1
        i += 1
    return k #len(upper)