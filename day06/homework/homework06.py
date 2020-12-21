"""
    在终端中获取颜色(RGBA),打印描述信息,否则提示颜色不存在
    "R" -> "红色"
    "G" -> "绿色"
    "B" -> "蓝色"
    "A" -> "透明度"
"""

dict_color = {"R": "红色",
              "G": "绿色",
              "B": "蓝色",
              "A": "透明度"
              }

color = input("请输入颜色：")

if color in dict_color:
    print(dict_color[color])
else:
    print("颜色不存在")
