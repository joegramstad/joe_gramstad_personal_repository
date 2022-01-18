def sum_recursive(digits):
    if len(digits) == 1:
        return digits[0]
    else:
        return digits[0] + sum_recursive(digits[1:])