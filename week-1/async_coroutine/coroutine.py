import asyncio

async def task_loader(sleep_time):
    print(f"Task started, sleeping for {sleep_time} seconds")
    await asyncio.sleep(sleep_time)
    return {"status": "completed", "sleep_time": sleep_time}



async def main():
    tasks = task_loader(2)
    print("Starting tasks...")

    result = await asyncio.gather(tasks)

    print(*result)
    print("All tasks completed.")



asyncio.run(main())