from .httpClient import HttpClient
from .model.enkaNetworkAPI import EnkaNetworkAPI
from .model.starrail import DetailInfo
from .types import Game
from .config import Config

class EnkaNetworkClient:
    def __init__(self, lang="ko"):
        if not lang in Config.LANG_LIST:
            raise ValueError(f"Unknown language: {lang}")
        Config.LANG = lang
        self.__http = HttpClient()

    async def fetch_genshin_user(self, uid: int, info: bool = False):
        data = await self.__http.fetch_user(uid, info, Game.GENSHIN)
        return EnkaNetworkAPI(**data)

    async def fetch_starrail_user(self, uid: int, info: bool = False):
        data = await self.__http.fetch_user(uid, info, Game.HONKAI_STARRAIL)
        return DetailInfo(**data["detailInfo"])
    
    async def update_genshin_assets(self):
        await self.__http.update_genshin_assets()

    async def update_starrail_assets(self):
        await self.__http.update_starrail_assets()