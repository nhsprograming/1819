(lambda total,groups: (lambda one,two,three,four: (lambda taxis: (lambda one: (lambda taxis: (lambda one: (lambda taxis: print(taxis))(taxis -(-one//4)))(max(0, one-two%2*2)))(taxis + two//2 + two%2))(max(0, one - three)))(four + three))(groups.count(1),groups.count(2),groups.count(3),groups.count(4)))(input(),list(map(int, input().split())))

#verified

# Method
# Count number of 4s, number of 3s and a equivilant number of 1s, number of 2s//2, 1- 2x 2s%2, ceiling number of 1s / 4
# input()
# groups = list(map(int, input().split()))
# one = groups.count(1)
# two = groups.count(2)
# three = groups.count(3)
# four = groups.count(4)
# taxis = four
# taxis = taxis + three
# one = max(0, one - three)
# taxis = taxis + two//2
# taxis = taxis + two%2
# one = max(0, one-two%2*2)
# taxis = taxis -(-one//4)
# print(taxis)