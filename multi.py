import random
import time

def task(value1):
    print('{} start'.format(value1))
    time.sleep(random.uniform(0.5, 1.0))
    print('{} end0'.format(value1[0]))
    print('{} end1'.format(value1[1]))
    return value1*2

from concurrent.futures import ThreadPoolExecutor

data= [[0,1],[2,3]]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(task,data))

print(results)


