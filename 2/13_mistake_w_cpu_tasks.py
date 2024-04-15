import asyncio
import functools
import time
from typing import Any, Callable


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f"выполняется {func} с аргументами {args} {kwargs}")
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f"{func} завершилась за {total:.4f} с")

        return wrapped

    return wrapper


async def delay(delay_seconds: int, name: str) -> int:
    print(f"задача {name} засыпает на {delay_seconds} с")
    await asyncio.sleep(delay_seconds)
    print(f"сон в течение {delay_seconds} для задачи {name} с закончился")
    return delay_seconds


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100000000):
        counter = counter + 1
    return counter


@async_timed()
async def main():
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())
    delay_task = asyncio.create_task(delay(4, "delay_task"))
    await task_one
    await task_two
    await delay_task


asyncio.run(main())
