import asyncio
from enkaNetwork.enkaNetworkClient import EnkaNetworkClient

client = EnkaNetworkClient()

async def main():
    genshin_data = await client.fetch_genshin_user(800036636)
    starrail_data = await client.fetch_starrail_user(800043041)

    print(genshin_data.model_dump_json())
    print(starrail_data.model_dump_json())

asyncio.run(main())