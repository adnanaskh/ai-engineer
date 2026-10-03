import asyncio


async def task_loader(id, sleep_time):
    print(f"Task {id} started, sleeped for {sleep_time} seconds")
    await asyncio.sleep(sleep_time)
    print(f"Task {id} finished after {sleep_time} seconds")

    return {"id": id, "status": "completed", "sleep_time": sleep_time}  


async def main():
    task1 = asyncio.create_task(task_loader(1, 2))
    task2 = asyncio.create_task(task_loader(2, 1))

    result1 = await task1
    result2 = await task2


    print(result1, result2)
    print("All tasks completed.")
asyncio.run(main())