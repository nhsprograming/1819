(lambda y: print('YES'*(any(x in y for x in ['1'*7,'0'*7])) or 'NO'))(input())

#verified