(lambda a: print([(abs(a.index(x)-2)+abs(x.index(1)-2)) for x in a if 1 in x][0]))([list(map(int, input().split())) for x in range(5)])

#verifed