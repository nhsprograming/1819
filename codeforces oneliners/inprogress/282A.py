(lambda y: print(sum([(1*("+" in i)-1*("-" in i)) for i in y])))([input() for x in range(int(input()))])

#verified