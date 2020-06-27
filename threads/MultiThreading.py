import threading
import time


class custom_thread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Started running thread: " + self.name)
        for i in range(4):
            time.sleep(1)
        print(self.name + " completed.")


def main():
    thread_1 = custom_thread("thread_1")
    thread_2 = custom_thread("thread_2")
    thread_3 = custom_thread("thread_3")
    thread_1.start()
    thread_2.start()
    thread_3.start()


if __name__ == "__main__":
    main()
