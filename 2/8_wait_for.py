import asyncio


async def delay(delay_seconds: int, name: str) -> int:
    print(f'задача {name} засыпает на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} для задачи {name} с закончился')
    return delay_seconds


async def main():
    delay_task = asyncio.create_task(delay(2, 'first'))
    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Тайм-аут!')
        print(f'Задача была снята? {delay_task.cancelled()}')

asyncio.run(main())
