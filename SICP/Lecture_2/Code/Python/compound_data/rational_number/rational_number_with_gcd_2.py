def make_rational_number(_numer, _denom):
    return [_numer, _denom]

def numer(rational_number):
    g = gcd(head(rational_number), tail(rational_number))
    return head(rational_number) / g

def denom(rational_number):
    g = gcd(head(rational_number), tail(rational_number))
    return tail(rational_number) / g

def add(rational_number1, rational_number2):
    return make_rational_number(
        numer(rational_number1) * denom(rational_number2) + denom(rational_number1) * numer(rational_number2),
        denom(rational_number1) * denom(rational_number2))

def mul(rational_number1, rational_number2):
    return make_rational_number(
        numer(rational_number1) * numer(rational_number2),
        denom(rational_number1) * denom(rational_number2))

def gcd(x, y):
    if y == 0:
        return x

    return gcd(y, x % y)

def head(pair):
    return pair[0]

def tail(pair):
    return pair[1]