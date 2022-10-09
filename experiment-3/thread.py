import time
from concurrent.futures import ThreadPoolExecutor

def cpu_task(x):
    count = 0
    for i in range(10**6):
        count += i

if __name__ == '__main__':
    marker_single = time.time()
    n_jobs = 4
    for i in range(n_jobs):
        cpu_task(i)
    print(f"Singlethread 花費: {time.time() - marker_single}")

    marker_multi = time.time()
    with ThreadPoolExecutor() as excutor:
        tasks = [1, 2, 3, 4]
        results = excutor.map(cpu_task, tasks)
    print(f"Multithreading 花費 : {time.time() - marker_multi}")