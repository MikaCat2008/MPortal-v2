import asyncio as aio

from app.server import Server


async def main() -> None:
    server = Server()

    await server.start()


if __name__ == "__main__":
    aio.run(main())
