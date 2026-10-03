import asyncio

async def task_loader(id, sleep_time):
    print(f"Task {id} started, sleeping for {sleep_time} seconds")
    await asyncio.sleep(sleep_time)
    print(f"Task {id} finished after {sleep_time} seconds")
    return {"id": id, "status": "completed", "sleep_time": sleep_time}


async def main():
    result = await asyncio.gather(
        task_loader(1, 2),
        task_loader(2, 3),
        task_loader(3, 1)
    )

    for res in result:
        print(res)
asyncio.run(main())