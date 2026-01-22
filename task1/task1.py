import asyncio

async def find_path(n, m):
    list_elem = [i for i in range(1, n+1)]
    list_interval = []
    interval = []
    i = 0
    start = 0
    while True:
        index = (start + i) % n
        interval.append(list_elem[index])
        i += 1
        if i == m:
            start += m-1
            i = 0
            list_interval.append(interval.copy())
            if index == 0:
                break
            interval = []
    return [interval[0] for interval in list_interval]


async def main():

    n, m = [int(elem) for elem in input().split()]
    n2, m2 = [int(elem) for elem in input().split()]
    task_one = asyncio.create_task(find_path(n, m))
    task_two = asyncio.create_task(find_path(n2, m2))
    result1, result2 = await asyncio.gather(task_one, task_two)
    print(*result1, *result2)

asyncio.run(main())
