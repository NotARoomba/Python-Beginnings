import math
def get_succession(x):
    return math.floor(x/10)+((x%10)*(x%10))
def problem1(x, y):
    for i in range(y):
        print(x)
        x = get_succession(x)
#def collatz_conjec#