"""
        在终端中累加 0  1  2  3
        在终端中累加 2  3  4  5  6
        在终端中累加 1  3  5  7
        在终端中累加 8  7  6  5  4
        在终端中累加 -1  -2  -3  -4  -5
"""

# 在终端中累加 0  1  2  3
count = 0
for i in range(4):
    count += i
print(count)

# 在终端中累加 2  3  4  5  6

count = 0
for i in range(2, 7):
    count += i
print(count)

# 在终端中累加 1  3  5  7

count = 0
for i in range(1, 8, 2):
    count += i
print(count)

# 在终端中累加 8  7  6  5  4

count = 0
for i in range(8, 3, -1):
    count += i
print(count)

# 在终端中累加 -1  -2  -3  -4  -5

count = 0
for i in range(-1, -6, -1):
    count += i
print(count)
