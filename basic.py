# Basic
for i in range(0,150+1):
    print(i)

# Multiples of Five
for i in range(0, 1000+1,5):
    print(i)

# Counting, the Dojo Way
for i in range(0,101,1):
    if i %10==0:
        print("Coding Dojo")
    elif i %5==0:
        print("Coding")
    else:
        print(i)

# Whoa. That's Sucker's Huge
odds = 0
for a in range(500000):
    if a % 2 != 0:
        odds = odds + a
print(odds)

# Countdown by Fours
for i in range(2018,0,-4):
    if i %2==0:
        print(i)

# Flexible Counter

low = 2
high = 10
mult = 3

for i in range(low,high):
    if i % mult ==0:
        print(i)
