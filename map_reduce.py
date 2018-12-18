from functools import reduce

def fn(x,y):
    return x * 10 + y

def char2num(s):
    digits = {
        '0' : 0,
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
    }
    print(s,type(s))
    print(digits[s],type(digits[s]))
    return digits[s]

if __name__ == "__main__":
    x = reduce(fn,map(char2num,'13579'))
    print(x)