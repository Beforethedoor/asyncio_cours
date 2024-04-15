import asyncio


async def delay(delay_seconds: int, name: str) -> int:
    print(f"задача {name} засыпает на {delay_seconds} с")
    await asyncio.sleep(delay_seconds)
    print(f"сон в течение {delay_seconds} для задачи {name} с закончился")
    return delay_seconds


async def main():
    sleep_for_three = asyncio.create_task(delay(3, "first"))
    print(type(sleep_for_three))
    result = await sleep_for_three
    print(result)


asyncio.run(main())
