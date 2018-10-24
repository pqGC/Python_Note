import secrets
import sys
import time
import os
import random

# 方法一：
alist = random.sample(range(220, 255), 35)  # random.sample()生成不相同的随机数
print(alist)
c = secrets.choice(alist)
print(c)

# 方法二：
csprng = random.SystemRandom()
i = csprng.randint(220, 255)
print(i)

# Random bytes

b = os.urandom(32)
print(b)

# 方法三：可能是安全随机数
t = int(time.time()**2) % 200
t2 = random.randint(0, 200)
print(t, t2)

print(time.time())
print(int(str(time.time())[-1]))  # 取时间戳最后一位

print(int(random.uniform(-dx, dx)))
