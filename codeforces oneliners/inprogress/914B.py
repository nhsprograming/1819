y = list(map(int, input().split()))
 
y.count(sorted(y)[-1])

print("Agasa"*(y.count(sorted(y)[-1])%2 == 0) + "Conan"*(y.count(sorted(y)[-1])%2 == 1))

(lambda x,y: print("Agasa"*(y.count(sorted(y)[-1])%2 == 0) + "Conan"*(y.count(sorted(y)[-1])%2 == 1)))(input(),list(map(int, input().split())))

#not a working solution method