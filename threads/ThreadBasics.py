import threading
import time


lock = threading.Lock()


def job(count, sleep_time):
    print(f'Started job: {count}')
    time.sleep(sleep_time)
    print(f'job: {count} completed')


# Example to show how threads are used and save time
time_start = time.perf_counter()
for j in range(1, 11):
    job(j, 1)
time_end = time.perf_counter()
time_taken = time_end-time_start
print(f'Finished in {round(time_taken, 2)} secs without threads.')

time_start = time.perf_counter()
threads = []
for j in range(1, 11):
    t = threading.Thread(target = job, args = [j, 1])
    t.start()
    threads.append(t)

# thread join makes sure that the execution time is calculated once all threads get executed,
# so, the code after join will be called after the thread with join method is done
for t in threads:
    t.join()
time_end = time.perf_counter()
time_taken = time_end-time_start
print(f'Finished in {round(time_taken, 2)} secs with threads.')


# Example showing how locks are performed
def job_lock(count, sleep_time):
    lock.acquire()
    print(f'Started job: {count}')
    time.sleep(1)
    print(f'job: {count} completed')
    lock.release()


for t in threads:
    t.join()
time_end = time.perf_counter()
time_taken = time_end-time_start
print(f'Finished in {round(time_taken, 2)} secs with threads having locks.')



