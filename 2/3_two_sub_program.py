import asyncio


async def delay(delay_seconds: int, name: str) -> int:
    print(f"задача {name} засыпает на {delay_seconds} с")
    await asyncio.sleep(delay_seconds)
    print(f"сон в течение {delay_seconds} для задачи {name} с закончился")
    return delay_seconds


async def add_one(number: int) -> int:
    return number + 1


async def hello_world_message() -> str:
    await delay(1, "first")
    return "Hello World!"


async def main() -> None:
    message = await hello_world_message()
    one_plus_one = await add_one(1)
    print(one_plus_one)
    print(message)


asyncio.run(main())
