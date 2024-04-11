import aiohttp
import aiofiles
from typing import Any
import json
from .config import Config
from .exception import *
from .types import Game

class Route:
    def __init__(self, method: str, path: str, endpoint: str = "enka"):
        self.method = method
        self.url = ""
        
        if endpoint == "enka":
            self.url = f"{Config.ENKA_PROTOCOL}://{Config.ENKA_API_URL}{path}"
        elif endpoint == "asset":
            self.url = f"{Config.ASSET_PROTOCOL}://{path}"

class HttpClient:
    async def request(self, r: Route):
        async with aiohttp.ClientSession() as s:
            async with await s.request(method=r.method, url=r.url) as res:
                if 300 > res.status >= 200:
                    return await res.json(content_type=None)
                else:
                    raise HttpException(f"{r.url}  status code: {res.status}")
                
    async def save_asset(self, path: str, data: Any):
        async with aiofiles.open(path, "w", encoding="UTF-8") as file:
            await file.write(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

    async def fetch_user(self, uid: int, info: bool, game: Game):
        r = Route(method="GET", path=f"/api{'/hsr' if game == Game.HONKAI_STARRAIL else ''}/uid/{uid}/{'?info' if info else ''}")
        return await self.request(r=r)

    async def update_genshin_assets(self):
        assetList = [Config.GITHUB_ASSET.CHARACTER,
                     Config.GITHUB_ASSET.LOC,
                     Config.GITHUB_ASSET.PFPS]
        
        for asset in assetList:
            r = Route(method="GET", path=Config.PATH.ASSET_GITHUB_PATH + asset, endpoint="asset")
            data = await self.request(r=r)
            await self.save_asset(path=Config.PATH.ASSET_FILE_PATH + asset, data=data)

        r = Route(method="GET", path=Config.PATH.ASSET_GITLAB_TEXTMAP_PATH + Config.GITLAB_ASSET.TEXTMAP_KR, endpoint="asset")
        textMapKr = await self.request(r=r)
        await self.save_asset(path=Config.PATH.ASSET_FILE_PATH + Config.GITLAB_ASSET.TEXTMAP_KR, data=textMapKr)

    async def update_starrail_assets(self):
        assetList = [Config.GITHUB_ASSET.STARRAIL_PFPS,
                     Config.GITHUB_ASSET.STARRAIL_CHARACTER,
                     Config.GITHUB_ASSET.STARRAIL_RELIC,
                     Config.GITHUB_ASSET.STARRAIL_SKILL,
                     Config.GITHUB_ASSET.STARRAIL_SKILLTREE,
                     Config.GITHUB_ASSET.STARRAIL_WEPS,
                     Config.GITHUB_ASSET.STARRAIL_LOC]
        
        for asset in assetList:
            r = Route(method="GET", path=Config.PATH.ASSET_GITHUB_PATH + asset, endpoint="asset")
            data = await self.request(r=r)
            await self.save_asset(path=Config.PATH.ASSET_FILE_PATH + asset, data=data)
