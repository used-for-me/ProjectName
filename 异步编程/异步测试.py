import asyncio
import time

a = [[], []]


# 定义异步方法
async def first_asyncio(n):
    a[0].append(n)
    print("first one.", n)
    # 异步休眠
    await asyncio.sleep(0)
    print("over first", n)
    a[1].append(n)

# 获取事件循环
loop = asyncio.get_event_loop()

# 异步队列
tasks = [first_asyncio(i) for i in range(100)]

# 计算时间
test1 = time.time()

# 运行队列
loop.run_until_complete(asyncio.wait(tasks))

# 计算时间
print(time.time() - test1)

# 关闭事件循环
loop.close()

# 开始异步顺序
print(a[0])

# 结束异步顺序
print(a[1])
