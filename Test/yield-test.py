# encoding:UTF-8
def yield_test(n):
    for a in range(n):
        yield a*2
        print("a=", a)
    # 做一些其它的事情
    print("do something.")
    print("end.")


# 使用for循环
for i in yield_test(3):
    print('i->', i)


