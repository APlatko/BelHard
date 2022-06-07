# import threading
#
#
# def doubler(number):
#     print(threading.currentThread().getName() + '\n')
#     print(number * 2)
#     print()
#
#
# if __name__ == "__main__":
#     for i in range(5):
#         my_thread = threading.Thread(target=doubler, args=(i,))
#         my_thread.start()

# import threading
# import time
#
# data = []
# lock = threading.RLock()
#
# def who_am_i(what):
#     print(f"Thread {threading.current_thread()} says: {what}")
#     lock.acquire()
#     global data
#     data.append(what)
#     time.sleep(2)
#     lock.release()
#
# if __name__ == "__main__":
#     for i in range(10):
#         thread = threading.Thread(target=who_am_i, args=(f"I'm function {i}",))
#         thread.start()
#     print(data)


# from threading import Condition, Thread
# from queue import Queue
# from time import sleep
#
# cv = Condition()
# q = Queue()
#
#
# def order_processor(name):
#     while True:
#         with cv:
#             while q.empty():
#                 cv.wait()
#             try:
#                 order = q.get_nowait()
#                 print(f"{name}: {order}")
#                 if order == "stop":
#                     break
#             except:
#                 pass
#             sleep(0.1)
#
#
# Thread(target=order_processor, args=("thread 1",)).start()
# Thread(target=order_processor, args=("thread 2",)).start()
# Thread(target=order_processor, args=("thread 3",)).start()
# for i in range(10):
#     q.put(f"order {i}")
# for _ in range(3):
#     q.put("stop")
# with cv:
#     cv.notify_all()


# from threading import Thread, BoundedSemaphore
# from time import time, sleep
#
# ticket_office = BoundedSemaphore(value=4)
#
# def tocket_buyer(number):
#     start_service = time()
#     with ticket_office:
#         sleep(1)
#         print(f" Client {number}, service time: {time() - start_service}")
#
# buyer = [Thread(target=tocket_buyer, args=(i,)) for i in range(5)]
# for b in buyer:
#     b.start()

# from threading import Thread, Event
#
# event  = Event()
#
# def worker(name: str):
#     event.wait()
#     print(f"Worker: {name}")
#
# event.clear()
# workers = [Thread(target=worker, args=(f"wrk {i}",)) for i in range(5)]
# for w in workers:
#     w.start()
# print("main thread")
# event.set()


# from threading import Timer
#
# timer = Timer(interval=3, function=lambda: print("Message from Timer"))
# timer.start()


# from threading import Barrier, Thread
# from time import sleep
#
# br = Barrier(3)
# store = []
#
# def f1(x):
#     print("calc")
#     store.append(x**2)
#     sleep(0.5)
#     br.wait()
#
# def f2(x):
#     print("calc 2")
#     store.append(x*2)
#     sleep(1)
#     br.wait()
#
# Thread(target=f1, args=(3,)).start()
# Thread(target=f2, args=(7,)).start()
#
# br.wait()
# print("Result", sum(store))


# from threading import Thread
# from time import sleep
#
#
# def func():
#     for i in range(5):
#         print(f"from child thread: {i}")
#         sleep(0.5)
#
#
# thread = Thread(target=func)
# thread.start()
# print("App stop")
# thread.join()
#
# print("\n")
# thread = Thread(target=func, daemon=True)
# thread.start()
# print("App stop")


# import multiprocessing
# import time
# import os
#
#
# def who_am_i(name):
#     print(f"i'm {name}, in process {os.getpid()}")
#
#
# def loopy(name):
#     who_am_i(name)
#     start = 1
#     stop = 1000000
#     for num in range(start, stop):
#         print(f"\tNumber of {num} of {stop}. Honk!")
#         time.sleep(1)
#
#
# if __name__ == "__main__":
#     who_am_i("i'm the main program")
#     process = multiprocessing.Process(target=loopy, args=("loopy",))
#     process.start()
#     for i in range(5):
#         print("Hi")
#         time.sleep(1)
#     process.terminate()


# import asyncio
#
#
# async def factorial(name, number):
#     f = 1
#     for i in range(2, number + 1):
#         print(f"Task {name}: Compute factorial({i})...")
#         await asyncio.sleep(1)
#         f *= i
#     print(f"Task {name}: factorial ({number}) = {f}")
#
#
# async def main():
#     await asyncio.gather(
#         factorial("A", 2),
#         factorial("B", 3),
#         factorial("C", 4),
#     )
#
#
# asyncio.run(main())


import asyncio
from time import time
import aiofiles
import aiohttp

URL = "https://loremflickr.com/320/240"


async def get_file(session: aiohttp.ClientSession):
    async with session.get(URL, allow_redirects=True) as response:
        data = await response.read()
        await write_file(data)


async def write_file(data):
    filename = f"file-{int(time() * 1000)}.jpeg"
    async with aiofiles.open("pic/" + filename, "wb") as file:
        await file.write(data)


async def main():
    t0 = time()
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            tasks.append(asyncio.create_task(get_file(session)))
        await asyncio.gather(*tasks)
    print(time() - t0)
    await asyncio.sleep(0.5)


if __name__ == "__main__":
    asyncio.run(main())
