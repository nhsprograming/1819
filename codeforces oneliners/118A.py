(lambda y: print('.'+'.'.join([l for l in y if l not in ('a', 'e', 'i', 'o', 'u', 'y')])))(input().lower())

#verified