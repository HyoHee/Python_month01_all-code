"""
    列表推导式：
        计算1970年到2050年之间所有闰年
"""

start_year = 1970
end_year = 2050


list_result = [i for i in range(start_year, end_year + 1)
               if i % 4 == 0 and i % 100 != 0 or i % 400 == 0]
print(list_result)
