import asyncio


async def delay(delay_seconds: int, name: str) -> int:
    print(f'задача {name} засыпает на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} для задачи {name} с закончился')
    return delay_seconds


async def main():
    sleep_for_three = asyncio.create_task(delay(3, 'first'))
    sleep_again = asyncio.create_task(delay(3, 'second'))
    sleep_once_more = asyncio.create_task(delay(3, 'last'))

    await sleep_again

asyncio.run(main())
