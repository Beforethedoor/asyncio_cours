import asyncio


async def delay(delay_seconds: int, name: str) -> int:
    print(f'задача {name} засыпает на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} для задачи {name} с закончился')
    return delay_seconds


async def hello_world() -> None:
    for i in range(5):
        await asyncio.sleep(1)
        print('Работаю пока другие спят!')


async def main() -> None:
    first_task = asyncio.create_task(delay(3, 'first_task'))
    second_task = asyncio.create_task(delay(3, 'second_task'))
    hello = asyncio.create_task(hello_world())

    await first_task
    await second_task
    await hello

asyncio.run(main())
