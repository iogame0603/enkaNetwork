import asyncio
from enkaNetwork.enkaNetworkClient import EnkaNetworkClient

client = EnkaNetworkClient()

async def main():
    # genshin_data = await client.fetch_genshin_user(800036636)

    starrail_data = await client.fetch_starrail_user(800036636)
    print(starrail_data)
    # for data in starrail_data.avatarInfoList:
    #     for relic in data.relicList:
    #         print(relic)

asyncio.run(main())