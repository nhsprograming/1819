import time # You can ignore this part

# Recap:

# print statement
print("Oranges are great")

# using variables
apples = "apples are great"

print(apples)

bestFruit = "none"

# if, else
if (apples == "apples are great"):
    bestFruit = "apples"
else:
    bestFruit = "oranges"

print(bestFruit)

userFavFruit = input("What is your favorite fruit (plural)? ")

# while loops
while (userFavFruit != bestFruit):
    userFavFruit = input("That is incorrect, what is your favorite fruit (plural)? ")

print("That is correct!")

# for loops
for i in range(10):
    print(i, "Apples are the best!!")

time.sleep(1.5) # You can ignore this part

# lists
x = [15,223,233,4744,552]

for i in range(2):
    if (i == 0):
        print("First time:")
    elif (i == 1):
        print("Second time:")
    for j in range(len(x)):
        print("i: ", i, " j: ", j, " x: ", x[j])
   
x.append(1923) # adds the value to the end of the array