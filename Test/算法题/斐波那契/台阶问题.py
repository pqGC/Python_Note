# 问题描述：
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

def fun1(n):
    fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)
    return fib


def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@memo
def fun2(i):
    if i < 2:
        return 1
    return fun2(i-1) + fun2(i-2)


def fun3(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    # print(fun1(3))
    print(fun2(3))
    # print(fun3(3))

