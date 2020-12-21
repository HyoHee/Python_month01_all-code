"""
        在终端中累加 0  1  2  3
        在终端中累加 2  3  4  5  6
        在终端中累加 1  3  5  7
        在终端中累加 8  7  6  5  4
        在终端中累加 -1  -2  -3  -4  -5
"""

# 在终端中累加0  1  2  3
count = 0
total = 0
while count < 4:
    total += count
    count += 1
print(total)

# 在终端中累加2  3  4  5  6
count = 2
total = 0
while count < 7:
    total += count
    count += 1
print(total)

# 在终端中累加1  3  5  7
count = 1
total = 0
while count < 8:
    total += count
    count += 2
print(total)

# 在终端中累加8  7  6  5  4
count = 8
total = 0
while count > 3:
    total += count
    count -= 1
print(total)

# 在终端中累加-1  -2  -3  -4  -5
count = -1
total = 0
while count > -6:
    total += count
    count -= 1
print(total)
