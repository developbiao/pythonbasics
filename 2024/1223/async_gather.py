import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")


async def main():
    # gather run multiple functino
    await asyncio.gather(task1(), task2())

# Run main function
if __name__ == "__main__":
    asyncio.run(main())
