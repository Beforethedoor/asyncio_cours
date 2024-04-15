import asyncio
import functools
import time
from typing import Any, Callable

import requests


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
async def get_example_status() -> int:
    return requests.get("http://www.example.com").status_code


@async_timed()
async def main():
    task_one = asyncio.create_task(get_example_status())
    task_two = asyncio.create_task(get_example_status())
    task_three = asyncio.create_task(get_example_status())
    delay_task = asyncio.create_task(delay(4, "delay_task"))
    await task_one
    await task_two
    await task_three
    await delay_task


asyncio.run(main(), debug=True)
