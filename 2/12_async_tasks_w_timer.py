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


@async_timed()
async def delay(delay_seconds: int) -> int:
    print(f"засыпаю на {delay_seconds} с")
    await asyncio.sleep(delay_seconds)
    print(f"сон в течение {delay_seconds} с закончился")
    return delay_seconds


@async_timed()
async def main():
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))
    await task_one
    await task_two


asyncio.run(main())
