"""
    生成10--30之间能被3或者5整除的数字
    [10, 12, 15, 18, 20, 21, 24, 25, 27]
"""

list_result = [i for i in range(10, 31) if
               i % 3 == 0 or i % 5 == 0]
print(list_result)
