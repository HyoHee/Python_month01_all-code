"""
    忒大装饰器返回值与参数
"""


def verify_permissions(func):
    def wrapper(*args,**kwargs):
        print("验证权限")
        re=func(*args,**kwargs)
        return re

    return wrapper

@verify_permissions
def insert():
    print("插入")
    return True

@verify_permissions
def delete(p1):
    print("删除")
    return False


# insert = verify_permissions(insert)
# delete = verify_permissions(delete)
print(insert())
print(delete())
