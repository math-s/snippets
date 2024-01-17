import asyncio
import time
import threading


def getFilenames(count):
    """
    Placeholder for fetching a list of filenames.
    """
    return [f"{i}.txt" for i in range(10)]


def readlines_block(filename):
    """
    Placeholder for a resource-bound file reader funcion.
    Returns file contents as a list of file lines.
    """
    num_of_lines = 10 + int(filename.split(".")[0])
    data = sum(i * i for i in range(10**6))
    res = [f"line - {i}: {data}" for i in range(num_of_lines)]
    return res


async def readlines(filename):
    """
    Placeholder for a resource-bound file reader funcion.
    Returns file contents as a list of file lines.
    """
    num_of_lines = 10 + int(filename.split(".")[0])
    data = sum(i * i for i in range(10**6))
    return [f"line - {i}: {data}" for i in range(num_of_lines)]


async def count_total_lines_(filenames) -> int:
    count = 0
    for file in filenames:
        count += len(await readlines(file))
    return count


async def count_total_lines(filenames) -> int:
    filelines = await asyncio.gather(*[readlines(file) for file in filenames])

    return sum([len(f) for f in filelines])


def count_total_lines_threading(filenames):
    threads = []

    results = {}

    def run(x):
        results[x] = len(readlines_block(x))

    for f in filenames:
        threads.append(threading.Thread(target=run, args=(f,)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    return sum(results.values())


if __name__ == "__main__":
    filenames = getFilenames(10)

    start = time.time()
    asyncio.run(count_total_lines(filenames))
    end = time.time()
    print(f"naive: {end - start}")

    start = time.time()
    asyncio.run(count_total_lines_(filenames))
    end = time.time()
    print(f"async: {end - start}")

    start = time.time()
    count_total_lines_threading(filenames)
    end = time.time()
    print(f"count_total_lines_threading: {end - start}")
