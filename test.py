import asyncio
from enkaNetwork.enkaNetworkClient import EnkaNetworkClient

client = EnkaNetworkClient()

async def main():
    await client.update_assets()
    data = await client.fetch_user(uid=800036636)
    print(data)

asyncio.run(main())