def xo(s):
    muchX = 0
    muchO = 0
    for i in s:
        if i == 'x' or i == 'X':
            muchX += 1
        elif i == 'o' or i == 'O':
            muchO += 1
        
    if (muchX == muchO):
        return True
    elif muchX == 0 and muchO == 0:
        return True
    else:
        return False