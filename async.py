import asyncio

async def action_1():
    print("First")

async def action_2():
    await asyncio.sleep(10)
    print("Second")

async def action_3():
    print("Third")

async def main():
    task_1 = asyncio.create_task(action_1())
    task_2 = asyncio.create_task(action_2())
    task_3 = asyncio.create_task(action_3())

    await asyncio.gather(task_1, task_2, task_3)

asyncio.run(main())
