import concurrent.futures
import time


def job(count, sleep_time):
    time.sleep(sleep_time)
    return f'job: {count} completed'


# using thread pool executor
with concurrent.futures.ThreadPoolExecutor() as executor:
    for i in range(1, 11):
        print(f'Submitting job: {i}')
        f = executor.submit(job, i, 1)
        print(f.result())

# Using comprehension
print("------------------------------------------------")
start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(job, i, 1) for i in range(1, 11)]
    [print(future.result()) for future in futures]
end = time.perf_counter()
print(f'{round(end - start)} secs taken to complete the task using comprehension.')
