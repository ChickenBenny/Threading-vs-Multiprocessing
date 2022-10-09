import time
import concurrent.futures
import matplotlib.pyplot as plt
import numpy as np

def tracker(x):
    start = time.time()
    list = []
    for i in range(10**6):
        list.append(time.time() - start)
    return list

def plot(results):
    for i, result in enumerate(results):
        plt.scatter(result, np.ones(len(result)) * i, alpha=0.8, c='red', edgecolors='none', s=1)
    plt.grid(axis='x')
    plt.ylabel("Tasks")
    ytks = range(3)
    plt.yticks(ytks, ['Task {}'.format(idx) for idx in ytks])
    plt.xlabel("Seconds")
    plt.title('Threading')
    plt.show()

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as excutor:
        tasks = [1, 2, 3]
        results = excutor.map(tracker, tasks)
        plot(results)