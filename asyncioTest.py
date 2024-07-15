import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)  # 模拟异步操作
    print("World")

async def main():
    await asyncio.gather(say_hello(), say_hello())

# 运行事件循环
asyncio.run(main())
