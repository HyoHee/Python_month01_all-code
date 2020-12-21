"""
    排列出两个骰子可以组成的所有可能
    排列出三个骰子可以组成的所有可能
"""
# list_result=[]
# for i01 in range(1,7):
#     for i02 in range(1,7):
#         list_result.append((i01,i02))
# print(list_result)
list_result = [(i01, i02) for i01 in range(1, 7) for i02 in range(1, 7)]
print(list_result)

# list_result = []
# for i01 in range(1, 7):
#     for i02 in range(1, 7):
#         for i03 in range(1, 7):
#             list_result.append((i01, i02,i03))
# print(list_result)

list_result = [(i01, i02, i03) for i01 in range(1, 7) for i03 in range(1, 7) for i02 in range(1, 7)]
print(list_result)
