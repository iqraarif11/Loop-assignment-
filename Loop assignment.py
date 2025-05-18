# Task 1: for loop
# This loop prints numbers from 1 to 10
for i in range(1 , 11):
    print(i)

# Task 2: While loop
i = 1
while i <= 5:
    print(i)
    i += 1

# Task 3: Loop with a condition
count = int(input("Enter a number:"))
while count >= 1:
    print(count)
    count -=1

# Task 4: Nexted loop
for i in range (1 , 4):
    for j in range (1 , 4):
        print(f"{i} * {j} = {i * j}")

# Task 5: break
for i in range (0 , 10):
    if i == 6:
        break
    print(i)

# Task 6: continue
for i in range (0 , 5):
    if i ==3:
        continue
    print(i)

# Bonus Task  :
word = input ("Enter a word: ")
for letter in word:
    print (letter)

