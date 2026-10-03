import asyncio

async def task_loader(id, sleep_time):
    print(f"Task {id} started, sleeping for {sleep_time} seconds")
    await asyncio.sleep(sleep_time)
    print(f"Task {id} finished after {sleep_time} seconds")
    return {"id": id, "status": "completed", "sleep_time": sleep_time}

async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 3, 1], start=1):
            tasks.append(tg.create_task(task_loader(i, sleep_time)))

    results = [task.result() for task in tasks]

    for res in results:
        print(res)

asyncio.run(main())