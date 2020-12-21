"""
    如果是vip客户,消费小于等于500,享受85折
                    消费大于500,享受8折
        如果不是vip客户,消费大于等于800,享受9折
                      消费小于800,原价
        在终端中输入账户类型,消费金额,计算折扣.
"""
genre = input("请输入客户类型：")
consume = float(input("请输入消费金额："))
if genre == "VIP":
    if consume >= 500:
        print("享受8折")
    else:
        print("享受85折")
else:
    if consume >= 800:
        print("享受9折")
    else:
        print("原价")
