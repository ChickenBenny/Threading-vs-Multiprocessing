from multiprocessing import Pool
import numpy as np
import time
import matplotlib.pyplot as plt

def cpu_task(x):
    start = time.time()
    count = 0
    for i in range(10 ** 8):
        count += 1
    stop = time.time()
    return start, stop

def plot(results):
    task = []
    for i in range(4):
        task.append(results[i, 1] - results[i, 0])
    plt.barh(['task1', 'task2', 'task3', 'task4'], task)
    plt.ylabel("Tasks")
    plt.xlabel("Seconds")
    plt.xlim(0, 13)
    plt.title('Multiprocessing')
    plt.show()

if __name__ == '__main__':
    with Pool(4) as p:
        tasks = [1, 2, 3, 4]
        results = p.map(cpu_task, tasks)
        plot(np.array(results))

