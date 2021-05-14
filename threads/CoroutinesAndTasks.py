import asyncio
import datetime
import time


# Creating a async method
async def job(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def coroutinesCall():
    print(f"coroutinesCall: started @ {datetime.datetime.now()}")
    await job(5, 'coroutinesCall:task1')
    await job(5, 'coroutinesCall:task2')
    print(f"coroutinesCall: finished @ {datetime.datetime.now()}")


# example using loop to schedule jobs
async def scheduleUsingLoop():
    loop = asyncio.get_running_loop()
    index = 1
    print(f"scheduleUsingLoop: started at {time.strftime('%X')}")
    while index <= 5:
        task = loop.create_task(job(5, 'scheduleUsingLoop:task{}'.format(index)))
        await task
        index = index + 1
    print(f"scheduleUsingLoop: ended at {time.strftime('%X')}")


async def createTask():
    # only to create task, task will start running only when await is called
    task1 = asyncio.create_task(job(5, 'createTask:task1'))
    task2 = asyncio.create_task(job(5, 'createTask:task2'))

    print(f"createTask: started at {time.strftime('%X')}")
    # Wait until both tasks are completed (should take around 2 seconds.)
    await task1
    await task2
    print(f"createTask: ran concurrently and finished at {time.strftime('%X')}")


async def scheduleUsingGather():
    # automatically scheduled items as a Task using gather()
    print(f"scheduleUsingGather: started at {time.strftime('%X')}")
    tasks = asyncio.gather(
        job(5, 'scheduleUsingGather:task1'),
        job(5, 'scheduleUsingGather:task2'),
        job(5, 'scheduleUsingGather:task3')
    )

    await tasks
    print(f"scheduleUsingGather: ended at {time.strftime('%X')}")


async def timeout():
    try:
        print(f"timeout: started @ {datetime.datetime.now()}")
        await asyncio.wait_for(scheduleUsingLoop(), timeout=5)
    except asyncio.TimeoutError:
        print(f"timeout: ended @ {datetime.datetime.now()}")


async def asCompleted():
    print(f"asCompleted: started @ {datetime.datetime.now()}")
    for jobItem in asyncio.as_completed({job(5, 'asCompleted:task1')}):
        result = await jobItem
        print(result)
    print(f"asCompleted: ended @ {datetime.datetime.now()}")


async def main():
    # print("---------------- Sequential calls ------------------")
    # await coroutinesCall()
    # print("                 -----------------                  ")
    # await scheduleUsingLoop()
    # print("---------------- Concurrent Calls ------------------")
    # await createTask()
    # print("                 -----------------                  ")
    # await scheduleUsingGather()
    # print("                 -----------------                  ")
    # await timeout()
    # print("                 -----------------                  ")
    await asCompleted()

asyncio.run(main())
