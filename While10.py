def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    sum_odd_digits = 0
    while i < len(s):
        if int(s[i]) % 2 == 1:
            sum_odd_digits += int(s[i])
        i += 1
    return sum_odd_digits