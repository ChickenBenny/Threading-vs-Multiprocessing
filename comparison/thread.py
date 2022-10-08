import time
import concurrent.futures
import matplotlib.pyplot as plt
import numpy as np

def cpu_task(x):
    start = time.time()
    count = 0
    for i in range(10 ** 8):
        count += 1
    stop = time.time()
    return start, stop

def plot(results):
    task = []
    for result in results:
        task.append(result[1] - result[0])
    plt.barh(['task1', 'task2', 'task3', 'task4'], task)
    plt.ylabel("Tasks")
    plt.xlabel("Seconds")
    plt.xlim(0, 13)
    plt.title('Threading')
    plt.show()

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as excutor:
        tasks = [1, 2, 3, 4]
        results = excutor.map(cpu_task, tasks)
        plot(results)