import multiprocessing
import time


def job(count, sleep_time):
    print(f'Started job: {count}')
    time.sleep(sleep_time)
    print(f'job: {count} completed')


def main():
    exec_times = [(1, 1), (2, 1), (3, 1), (4, 1)]
    start = time.perf_counter()
    processes = []
    for i in range(1, 11):
        p = multiprocessing.Process(target = job, args=exec_times)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
    end = time.perf_counter()
    print(f'{round(end-start)} secs taken to complete the task.')


if __name__ == '__main__':
    main()

