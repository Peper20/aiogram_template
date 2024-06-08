from asyncio import run


from app.main import start_app




async def main() -> None:
    await start_app()

run(main())

