#print prime numbers until the user tells you to stop

choice = input("Next prime number?")
current = 1

def checkPrime(n):
  if n == 2:
    return True
  if n%2 == 0:
    return False
  for i in range(3, int((int(n))**0.5)+1, 2):
    if n % i == 0:
      return False
  return True

while choice.lower().startswith("y"):
  current = int(input("PLease Input a number"))
  print(checkPrime(current)) 
  choice = input("Continue?")
