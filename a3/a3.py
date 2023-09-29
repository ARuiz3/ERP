def longest(a1, a2):
    res = ''
    a = a1 + a2
    for i in a:
        if i not in res:
            res += i
    finalres =''.join(sorted(res))
    return (finalres)
