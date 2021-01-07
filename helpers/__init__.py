

def parsFloat(numb):
    st = str(numb)
    ab = abs(numb)
    if(st[0] == '-'):
        return -ab
    return ab