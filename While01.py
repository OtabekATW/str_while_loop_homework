def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    n = 0
    while i < len(s):
        n += s[i].isdigit()

        i += 1
    return n