"""
    温度转换器：
    摄氏度 = （华氏度 - 32） 除以 1.8
    在终端中录入摄氏度，计算华氏度
"""
degree01 = float(input("请输入摄氏度："))
degree02 = degree01 * 1.8 + 32
print("华氏度是："+str(degree02))
