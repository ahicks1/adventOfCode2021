def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

def doesEqual(expected, actual):
    if(expected == actual):
        prGreen(f"Passed: expected {expected} got {actual}")
    else:
        prRed(f"Failed: expected {expected} got {actual}")