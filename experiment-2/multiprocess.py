from multiprocessing import Pool
import numpy as np
import time
import matplotlib.pyplot as plt

def tracker(x):
    start = time.time()
    list = []
    for i in range(10**6):
        list.append(time.time() - start)
    return list

def plot(results):
    print("success")
    for i, result in enumerate(results):
        plt.scatter(result, np.ones(len(result)) * i, alpha=0.8, c='red', edgecolors='none', s=1)
    plt.grid(axis='x')
    plt.ylabel("Tasks")
    ytks = range(3)
    plt.yticks(ytks, ['Task {}'.format(idx) for idx in ytks])
    plt.xlabel("Seconds")
    plt.title('Multiprocessing')
    plt.show()

if __name__ == '__main__':
    with Pool(3) as p:
        tasks = [1, 2, 3]
        results = p.map(tracker, tasks)
        plot(np.array(results))

