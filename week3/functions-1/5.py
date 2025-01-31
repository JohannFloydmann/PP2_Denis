def permutations(st, cur=""):
    if not st:
        print(cur)
        return
    
    for i in range(len(st)):
        permutations(st[:i] + st[i+1:], cur + st[i])

permutations("abc")