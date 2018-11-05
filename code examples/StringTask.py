#Codeforces118A
word  = input()
word = word.lower()
letters = list(word)
vowels = ['a','e','i','o','u','y']
result = []
print(letters)

for i in letters:
  if (i not in vowels):
    result.append("."+i)
print((result))
print("".join(result))
