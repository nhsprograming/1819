v = list(input())
hello = False

if "h" in v: 
    v = v[v.index('h')+1:]
    if "e" in v: 
        v = v[v.index('e')+1:]
        if "l" in v: 
            v = v[v.index('l')+1:]
            if "l" in v: 
                v = v[v.index('l')+1:]
                if "o" in v: 
                    hello = True

print("YES"*hello or "NO")

(lambda v: (lambda v: (lambda v: (lambda v: (lambda v: print("YES"*hello or "NO"))(if "o" in v: v=[v.index('o')+1:]))(if "l" in v: v=[v.index('l')+1:]))(if "l" in v: v=[v.index('l')+1:]))(if "e" in v: v=[v.index('e')+1:]))(if "h" in v: v=[v.index('h')+1:])(lambda v,hello: )(list(input()),False)





