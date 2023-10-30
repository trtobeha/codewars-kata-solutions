import test

info = {
    'source' : 'https://www.codewars.com/kata/5503013e34137eeeaa001648/train/python',
    'kata-level' : 6,
}

# Instructions:
#You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters.
# Trailing spaces should be removed, and every line must be terminated with a newline character (\n).
#Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.


# Solution:
def diamond(n):

    if n < 1 or not n % 2:
        return None
    s = ''
    for i in range(n):
        a = '*'*(i*2 + 1) if i <= n/2 else '*'*((n-i)*2 - 1)
        s += ' '*int((n-len(a)) / 2) + a + '\n'
    return s

# diamond(9)

# tests:

def test_my_solution():
    # expected =  " *\n"
    # expected += "***\n"
    # expected += " *\n"
    # assert diamond(1) == "*\n"
    assert diamond(2) == None
    # assert diamond(3) == expected
    assert diamond(5) == "  *n ***\n*****\n ***\n  *\n"
    assert diamond(0) == None
    assert diamond(6) ==  None
    assert diamond(2) == None



test_my_solution()
diamond(1)