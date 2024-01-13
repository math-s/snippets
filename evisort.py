import asyncio
from decorator import measure_time


def getFilenames(count):
    """
    Placeholder for fetching a list of filenames.
    """
    return [f"{i}.txt" for i in range(10)]


def readlines(filename):
    """
    Placeholder for a resource-bound file reader funcion.
    Returns file contents as a list of file lines.
    """
    num_of_lines = 10 + int(filename.split(".")[0])
    data = sum(i * i for i in range(10**6))
    return [f"line - {i}: {data}" for i in range(num_of_lines)]


@measure_time
def count_total_lines(filenames) -> int:
    count = 0
    for file in filenames:
        count += len(readlines(file))
    return count



@measure_time
async def async_count_total_lines(filenames) -> int:
    count = 0
    for file in filenames:
        count += len(await asyncio.to_thread(readlines, file))
    return count


if __name__ == "__main__":
    filenames = getFilenames(10)

    count_total_lines(filenames)
    async_count_total_lines(filenames)
